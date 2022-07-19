from email.mime import image
from flask import Flask, render_template, url_for, request, abort

app = Flask(__name__)

#response = request.get("https://imdb-api.com/en/API/IMDbList/k_zqtxyfc4/ls004285275")
#content = response.json()




class File:
    def __init__(self, title, length, type):
        self.title = title
        self.length = length
        self.type = type
    type = "movie"
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
    File.title = movietitle
    return render_template("EachMovie.html", movie = File)

@app.route("/categories/<category>")
def categories(category):
    if category not in choice:
       return render_template("404Error.html")
        
    p1 = File("as", 50, "movie")
    p1.category = ["horror" , "comedy"]
    p2 = File("aas", 50, "movie")
    p2.category = ["horror" , "comedy"]
    p3 = File("abs", 50, "movie")
    p3.category = ["horror" , "comedy"]
    index = [p1,p2,p3]
    if index[0].type == "movie":
        return render_template("categories.html", index = index, category = category, type = "movie")
    elif index[0].type == "book":
        return render_template("categories.html", index = index, category = category, type = "book")
    elif index[0].type == "serie":
        return render_template("categories.html", index = index, category = category, type = "serie")
    else: 
        return "error"
app.run(debug=True)
