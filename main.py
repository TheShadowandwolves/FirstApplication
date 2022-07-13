from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books():
    return render_template("Books.html")

@app.route("/movies")
def movies():
    return render_template("Movies.html")

@app.route("/series")
def series():
    return render_template("Series.html")

@app.route("/project")
def project():
    return render_template("Project.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/terms")
def terms():
    return render_template("Terms&Conditions.html")



app.run(debug=True)
