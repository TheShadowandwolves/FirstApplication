from email.mime import image
from flask import Flask, render_template, url_for, request, abort, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from search import getBestMovie, getFoundMoviesbyName, getFoundMoviesbyID, getMoviewithID, getCategory, getRating, getlength, user_input, data
from registration import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)




#search.getMovie("pirates")
#movie = getMoviewithID(id)

app.config['SECRET_KEY'] = 'mysecret1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    # wish_list = db.relationship('Wish_list', backref='author', lazy=True)
    # watched_list = db.relationship('Watched_list', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     movie_Id = db.Column(db.String(10), nullable=False, unique = True)

#     def __repr__(self):
#         return f"MovieList('{self.movie_Id}')"

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

bookts = [File("shadowhunter", 555, "book",["horror", "fantasy"]),File("lol", 33, "book", ["horror", "comedy"]),File("dld", 555, "book",["horror", "action"]), File("freeky", 555, "book",["horror", "other"]),File("gig", 555, "book",["horror", "comedy"])]
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
    book = bookts
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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index', name='Admin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger') 
    return render_template("login.html", title = 'Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index', name = form.username._value()))
    return render_template("register.html", title='Register', form=form)

@app.route("/about")
def about():
    return render_template("about.html")

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

if __name__ == '__main__':     
    app.run(debug=True)
