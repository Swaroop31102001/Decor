# Diagnostic Report: Automatic Session Logouts

## Executive Summary
After a thorough analysis of the authentication logic in the application, the root cause of the automatic logouts after a period of inactivity has been successfully identified as **server-side session clearing (Garbage Collection mismatch)**. The application exclusively uses native PHP sessions for state management without external platforms like Firebase or short-lived JWTs. 

Although the application explicitly requests a 2-day session lifetime, the server's default configuration aggressively deletes these sessions after roughly 24 minutes of inactivity due to how PHP handles session storage paths across different scripts.

---

## Technical Findings

### 1. Authentication Strategy
The application uses pure PHP native sessions to track user authentication, managed primarily through:
- `admin_login.php` (and similar login endpoints) to authenticate credentials and populate `$_SESSION`.
- `includes/session_init.php` to start the session, configure session runtime settings, and manage cookies.
- `includes/user_usage_tick.php` to occasionally update the session on navigation.

The search phase confirmed the **absence** of:
- Firebase Auth SDKs or listeners.
- Client-side token validation (e.g., JSON Web Tokens stored in `localStorage` or cookies).
- Frontend timeouts invoking a redirect to `login.html`.

### 2. Session Configuration (`includes/session_init.php`)
The `session_init.php` file attempts to configure a long-lived session:

```php
$lifetime = 86400 * 2; // 2 days
ini_set('session.gc_maxlifetime', (string)$lifetime);
```

While the cookie correctly receives a 2-day expiration in the client's browser, the issue resides entirely server-side.

### 3. The Trigger: Shared Local Temp Directory
In standard PHP environments (particularly on centralized servers or XAMPP on Windows), PHP stores all session files in a single, default temporary directory (`session.save_path` — usually `C:\xampp\tmp` or `/tmp`).

PHP utilizes a **Garbage Collector (GC)** that frequently runs on incoming requests to clean up abandoned session files. The GC behaves in the following way:
1. When a user is inactive, their session file on the server stops receiving "last modified" timestamp updates.
2. If *any other* PHP application or endpoint running on the same server invokes `session_start()` without the custom `86400 * 2` override, it starts the garbage collector using the system's default `session.gc_maxlifetime` (which is typically `1440` seconds, or **24 minutes**).
3. The global GC scans the shared temporary directory and permanently **deletes or clears** your application's session file because it thinks the file is "expired" (older than 24 minutes), blatantly ignoring the 2-day local override. 

When the user attempts their next action, the application verifies `$_SESSION['is_logged_in']` but finds the session file empty/non-existent. The session "comes out", triggering the generic security fallback block (usually found at the top of dashboard files):
```php
if (!isset($_SESSION['is_logged_in'])) {
    header("Location: login.html");
    exit;
}
```

### 4. Continuous Activity Mitigation
There is an implicit safety net when the user is actively working: `includes/user_usage_tick.php`.
```php
$_SESSION['app_usage_prev_clock'] = $now;
```
Every time an eligible user navigates securely, the script modifies the `$_SESSION` variable. This constantly "touches" the underlying session file, refreshing its modification timestamp and saving it from the 24-minute GC limit. This explains why the logout exclusively happens **after a period of inactivity**, but not while they are frequently clicking around.

---

## Proposed Remediation (No Modifications Applied)
To fix this behavior permanently, the application needs to isolate its session files into a dedicated storage location, immune to external garbage collection sweeps.

1. **Custom Session Save Path**: Add `ini_set('session.save_path', __DIR__ . '/sessions');` immediately before `ini_set('session.gc_maxlifetime', ...)` within `session_init.php`. 
2. Ensure the `/sessions` directory exists locally on the disk with proper read/write permissions.

*Constraint Note: As requested, no files were modified and the application remains functionally untouched.*
