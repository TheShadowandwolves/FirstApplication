from email.mime import image
from flask import Flask, render_template, url_for, request, abort, redirect, flash
from search import getBestMovie, getFoundMoviesbyName, getFoundMoviesbyID, getMoviewithID, getCategory, getRating, getlength, user_input, data
from registration import RegistrationForm, LoginForm

app = Flask(__name__)

# response = request.get('https://imdb-api.com/en/API/IMDbList/k_zqtxyfc4/ls004285275')
# content = response.json()


#search.getMovie("pirates")
#movie = getMoviewithID(id)

app.config['SECRET_KEY'] = 'mysecret1234'

class Data:
    def __init__(self, movie):
        self.title = movie['title']
        self.length = movie['runtime']
        self.category = movie['genres']
        self.rating = movie['rating']
        self.publishDate = movie['year']
        self.language = movie['languages']
        self.description = movie['plot']
        self.image = movie['poster']

class File:
    def __init__(self, title, length, type, cat):
        self.title = title
        self.length = length
        self.type = type
        self.category = cat
        
        
    type = "movie"
    title = "amb"
    qualitiy = "1080p"
    rating = 5
    publishdate = 2020
    length = 60
    language = ["german", "english", "french"]
   
    description = "none"
    screenshots = []
    image = "none"

choice = ["action", "horror", "comedy", "drama", "kids", "fantasy","other"]

# def getMovieData(movie):
#     data = movie
#     return data


@app.route("/home/<name>")
@app.route("/<name>")
def index(name):
    mylist = [1,2,3,4,5]

    return render_template("index.html", name=name)

@app.route("/books")
def books():
    book = [File("shadowhunter", 555, "book",["horror", "fantasy"]),File("lol", 33, "book", ["horror", "comedy"])]
    return render_template("Books.html", category = choice, book = book)

@app.route("/movies")
def movies():
    movies = getBestMovie()
    return render_template("Movies.html", movies = movies)

@app.route("/series")
def series():
    return render_template("Series.html")

@app.route("/project")
def project():
    return render_template("Project.html")

@app.route("/about")
def about():
    form = LoginForm()
    return render_template("About.html", title = 'Login', form = form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index', name = form.username._value()))
    return render_template("register.html", title='Register', form=form)

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
        
    p1 = File("as", 50, "movie", ["horror" , "comedy"])
    
    p2 = File("aas", 50, "movie", ["horror" , "comedy"])
  
    p3 = File("abs", 50, "movie", ["horror" , "comedy"])
    
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
