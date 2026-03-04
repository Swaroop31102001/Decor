from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/services")
def services():
    return render_template("index.html")

@app.route("/activities")
def activities():
    return render_template("index.html")

@app.route("/interactive")
def interactive():
    return render_template("index.html")

@app.route("/snacks")
def snacks():
    return render_template("index.html")

@app.route("/flower-decor")
def flower_decor():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
