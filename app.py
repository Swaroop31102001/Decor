import os
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

def get_all_images():
    categories = {
        'grand': 'grand theme',
        'sequin': 'Sequin decors',
        'simple': 'simple decor',
        'theme': 'theme decor'
    }
    all_images = {}
    for key, folder in categories.items():
        image_dir = os.path.join(app.static_folder, 'images', folder)
        if os.path.exists(image_dir):
            all_images[key] = sorted([f"{folder}/{f}" for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    return all_images

@app.route("/")
def home():
    return render_template("index.html", images=get_all_images())

@app.route("/gallery")
def gallery():
    return render_template("index.html", images=get_all_images())

@app.route("/services")
def services():
    return render_template("index.html", images=get_all_images())

@app.route("/activities")
def activities():
    return render_template("index.html", images=get_all_images())

@app.route("/interactive")
def interactive():
    return render_template("index.html", images=get_all_images())

@app.route("/snacks")
def snacks():
    return render_template("index.html", images=get_all_images())

@app.route("/flower-decor")
def flower_decor():
    return render_template("index.html", images=get_all_images())

@app.route("/contact")
def contact():
    return render_template("index.html", images=get_all_images())

if __name__ == "__main__":
    app.run(debug=True)
