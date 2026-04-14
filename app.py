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

activities_db = {
    "magic-balloon-twisting": {
        "title": "Magic Balloon Twisting",
        "image": "Activities/Balloon sculpture.jpg",
        "description": "Watch in awe as our expert artists twist and shape colorful balloons into amazing animals, swords, and whimsical characters. Perfect for adding a touch of magic to any party!"
    },
    "custom-bracelet-bar": {
        "title": "Custom Bracelet Bar",
        "image": "Activities/Bracelet making.jpg",
        "description": "Let your guests unleash their creativity! Our custom bracelet making station comes with a huge variety of colorful beads, charms, and letters to craft the perfect personalized keepsake."
    },
    "comical-caricatures": {
        "title": "Comical Caricatures",
        "image": "Activities/Caricature on paper.jpg",
        "description": "Capture the laughter and joy of your event with our talented caricature artists. Guests get to take home a hilarious and personalized drawn portrait that they'll cherish forever."
    },
    "personalized-keychain-crafting": {
        "title": "Personalized Keychain Crafting",
        "image": "Activities/Keychain Making.jpg",
        "description": "A fun and interactive activity where guests design and assemble their very own keychains. We provide all the fun trinkets and tools needed to create a unique party favor."
    },
    "elegant-name-plates": {
        "title": "Elegant Name Plates",
        "image": "Activities/Name Plate.jpg",
        "description": "Guests can design and personalize their very own beautiful name plates! A creative and fun way to make a gorgeous room decor item they can take home."
    },
    "creative-pebble-art": {
        "title": "Creative Pebble Art",
        "image": "Activities/Pebble art.jpg",
        "description": "Bring nature and art together! Discover the joy of pebble painting and arrangement. This relaxing and creative activity is wonderful for guests of all ages to express themselves."
    },
    "beautiful-pot-painting": {
        "title": "Beautiful Pot Painting",
        "image": "Activities/Pot painting.jpg",
        "description": "Let colors fly as your guests paint and decorate their very own ceramic pots. A delightfully messy and creative activity that results in a lovely customized planter."
    },
    "fun-face-painting": {
        "title": "Fun Face Painting",
        "image": "Activities/Tatto1.jpg",
        "description": "Transform into superheroes, beautiful butterflies, or fierce tigers! Our professional face painters bring incredible designs and smiles to every party."
    },
    "cool-temporary-tattoos": {
        "title": "Cool Temporary Tattoos",
        "image": "Activities/Tattoo.jpg",
        "description": "Add some edgy and colorful flair to your celebration! Our temporary tattoo station offers a wildly popular selection of fun, safe, and easily removable designs for everyone."
    },
    "creative-clay-modeling": {
        "title": "Creative Clay Modeling",
        "image": "Activities/clay modeling.jpg",
        "description": "Squish, roll, and create! Our clay modeling activity lets kids and adults mold their imagination into fun, cute, and fantastic tiny sculptures."
    },
    "artistic-jewellery-making": {
        "title": "Artistic Jewellery Making",
        "image": "Activities/jewllery making.jpg",
        "description": "Unleash the inner designer! Guests can string together beautiful necklaces and accessories using our wide assortment of dazzling charms and beads."
    },
    "hands-on-pottery": {
        "title": "Hands-On Pottery",
        "image": "Activities/pottery.jpg",
        "description": "Get your hands dirty and learn the ancient art of pottery! A thrilling and super tactile experience where guests mold their very own clay bowls and cups."
    },
    "squishy-slime-making": {
        "title": "Squishy Slime Making",
        "image": "Activities/slime making.jpg",
        "description": "The ultimate party favorite! Kids go crazy for our interactive slime making station where they get to mix colors, add glitter, and create the perfect squishy masterpiece."
    },
    "fridge-magnet-making": {
        "title": "Fun Fridge Magnet Crafting",
        "image": "Activities/fridge magnet making.jpg",
        "description": "A delightful hands-on craft where children paint and design their own colorful fridge magnets. A beautiful personalized memento to take home and stick on the fridge!"
    },
    "puppet-show": {
        "title": "Entertaining Puppet Show",
        "image": "Activities/Puppet Show.jpg",
        "description": "Gather around for an interactive, storytelling adventure! Our engaging puppet shows captivate imaginations with fun characters, silly voices, and wonderful interactive tales."
    },
    "crown-making": {
        "title": "Royal Crown Making",
        "image": "Activities/Crown Making.jpg",
        "description": "Every child is royalty for the day! Let them build, decorate and bedazzle their own majestic crowns using jewels, glitter, and vibrant colors before wearing them proudly."
    },
    "professional-mc": {
        "title": "Professional Event MC",
        "image": "Activities/MC.jpg",
        "description": "Keep the energy high and the guests entertained! Our professional MCs host engaging games, coordinate the flow of events, and ensure everyone is having a spectacular time."
    },
    "live-dj": {
        "title": "Live DJ Experience",
        "image": "Activities/Live DJ.jpg",
        "description": "Get the party moving with our incredible live DJ setup! We bring the best mixes, high-quality audio equipment, and a phenomenal atmosphere to keep the dance floor packed."
    }
}

snacks_db = {
    "chocolate-fountain": {
        "title": "Chocolate Fountain",
        "image": "Snacks/choclate fountain.jpg",
        "description": "Indulge in our luxurious flowing chocolate fountain! Complete with marshmallows, fresh fruits, and wafers for an unforgettable sweet experience."
    },
    "cotton-candy": {
        "title": "Cotton Candy",
        "image": "Snacks/cotton candy.jpg",
        "description": "Bring back childhood memories with our fluffy, melt-in-your-mouth cotton candy. Spun fresh on-site in a variety of vibrant colors and flavors!"
    },
    "ice-gola": {
        "title": "Ice Gola",
        "image": "Snacks/ice gola.jpg",
        "description": "Beat the heat with our refreshing traditional Ice Golas! Crushed ice infused with dozens of tangy, sweet, and mesmerizing colorful syrups."
    },
    "fresh-popcorn": {
        "title": "Fresh Popcorn",
        "image": "Snacks/pop corn.jpg",
        "description": "No party is complete without the irresistible aroma of freshly popped buttery popcorn. We provide unlimited servings from our classic popcorn cart!"
    },
    "sweet-corn": {
        "title": "Sweet Corn",
        "image": "Snacks/sweet corn.jpg",
        "description": "Hot, buttery, and deliciously spiced! Our sweet corn stall offers the perfect savory treat for guests looking for a wholesome snack."
    }
}

@app.route("/")
def home():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/gallery")
def gallery():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/services")
def services():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/activities")
def activities():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/interactive")
def interactive():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/snacks")
def snacks():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/flower-decor")
def flower_decor():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/contact")
def contact():
    return render_template("index.html", images=get_all_images(), activities=activities_db, snacks=snacks_db)

@app.route("/activity/<slug>")
def activity_detail(slug):
    activity = activities_db.get(slug)
    if not activity:
        return "Activity not found", 404
    return render_template("activity.html", activity=activity)

@app.route("/snack/<slug>")
def snack_detail(slug):
    snack = snacks_db.get(slug)
    if not snack:
        return "Snack not found", 404
    return render_template("snack.html", snack=snack)

if __name__ == "__main__":
    app.run(debug=True)
