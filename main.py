from email.mime import image
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

class movie:
    def __init__(self, title, length):
        self.title = title
        self.length = length
    title = "amb"
    qualitiy = "1080p"
    rating = 5
    publishdate = 2020
    length = 60
    language = ["german", "english", "french"]
    category = ["horror", "comedy"]
    description = "none"
    screenshots = []
    image = "none"

choice = ["action", "horror", "comedy", "drama", "kids", "other"]

def getMovieData(movie):
    data = movie
    return data


@app.route("/home/<name>")
@app.route("/<name>")
def index(name):
    mylist = [1,2,3,4,5]

    return render_template("index.html", name=name)

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

@app.route("/eachMovie/<movietitle>")
def eachMovie(movietitle):
    movie.title = movietitle
    return render_template("EachMovie.html", movie = movie)

@app.route("/categories/<category>")
def categories(category):
    p1 = movie("as", 50)
    p1.category = ["horror" , "comedy"]
    p2 = movie("aas", 50)
    p2.category = ["horror" , "comedy"]
    p3 = movie("abs", 50)
    p3.category = ["horror" , "comedy"]
    movieindex = [p1,p2,p3]
    
    return render_template("categories.html", movieindex = movieindex, category = category)



app.run(debug=True)
