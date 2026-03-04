import os
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

def get_images():
    image_dir = os.path.join(app.static_folder, 'images')
    if os.path.exists(image_dir):
        # Sort files to keep order consistent
        return sorted([f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    return []

@app.route("/")
def home():
    return render_template("index.html", images=get_images())

@app.route("/gallery")
def gallery():
    return render_template("index.html", images=get_images())

@app.route("/services")
def services():
    return render_template("index.html", images=get_images())

@app.route("/activities")
def activities():
    return render_template("index.html", images=get_images())

@app.route("/interactive")
def interactive():
    return render_template("index.html", images=get_images())

@app.route("/snacks")
def snacks():
    return render_template("index.html", images=get_images())

@app.route("/flower-decor")
def flower_decor():
    return render_template("index.html", images=get_images())

@app.route("/contact")
def contact():
    return render_template("index.html", images=get_images())

if __name__ == "__main__":
    app.run(debug=True)
