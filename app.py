from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Data for placement opportunities
placement_opportunities = [
    {
        "title": "Internship Program",
        "description": "A six-month internship program with a leading organization.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCxl9WM74ONRXV3CTQ3DWGX6xeLC5qvLftELfCsYRf2tDjtJrwTCgJCK4&s",
        "placements_per_year": 1587
    },
    {
        "title": "Skill Training Program",
        "description": "Learn essential workplace skills and boost your career prospects.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_xJMbotMWUG4ucTGOCEcymgfrrML4u7O2YVe-f9r7-MZGdzQIJIEJWs4&s",
        "placements_per_year": 1824
    },
    {
        "title": "Placement Assistance",
        "description": "Direct placement opportunities with reputed companies.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBg94viE3aMAhph-HX4h_IludYCz2F7LgsCYJsJfCv-fZifKrgt3vphQs&s",
        "placements_per_year": 1725
    },
]

# Data for social welfare activities
social_activities = [
    {
        "title": "Food Distribution",
        "description": "Distributing food to orphaned children and the underprivileged.",
        "image": "https://st3.depositphotos.com/26566316/32164/i/450/depositphotos_321647860-stock-photo-free-food-needs-refugees-food.jpg",
    },
    {
        "title": "Fruits Donation",
        "description": "Providing fresh fruits to ensure nutrition and health.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIaxoVVa7pqBhcvtKjnzBG8IyaTzVB8hzLiCrrtpLH2D064-L4SzpA-8k&s",
    },
    {
        "title": "Clothing Drive",
        "description": "Collecting and distributing clothing to those in need.",
        "image": "https://greenchoicelifestyle.com/wp-content/uploads/2024/09/Donated-clothes-get-thrown-away.jpg",
    },
]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", activities=social_activities)

@app.route("/donate", methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        donor_name = request.form.get("name")
        amount = request.form.get("amount")
       
    return render_template("donate.html")

@app.route("/placement-opportunities")
def placement_opportunities_view():
    return render_template("placement_opportunities.html", opportunities=placement_opportunities)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        
    return render_template("contact.html")

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)),debug=True)

