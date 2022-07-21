from email.mime import image
import string
from flask import Flask, render_template, url_for, request, abort
import imdb
ia = imdb.Cinemagoer()
app = Flask(__name__)

# gets the movies from the imdb api with the given name
@app.route('/data/<name>', methods=['GET', 'POST'])
def data(name):
    if request.method == 'POST':
        return user_input(name)
    else:
        return "error"
# gets the movies from the imdb api with the given id
@app.route('/data/<id>', methods=['GET', 'POST'])
def data2(id):
    if request.method == 'POST':
        return getFoundMoviesbyID(id)
    else:
        return "error"

# user_movie_input = "Pirates"

# movies = ia.search_movie(user_movie_input)


# for movie in movies:
#     print(movie['title'])
# reads the user input and returns the movies with the given name
def user_input(input):
    user_movie_input = input
    return getFoundMoviesbyName(user_movie_input)

#gets movie with the given id
def getFoundMoviesbyID(id):
    movie = ia.get_movie(id)
    return movie

# gets the movies from the imdb api with the given name
def getFoundMoviesbyName(user_movie_input):
    movies = ia.search_movie(user_movie_input)
    for movie in movies:
        ia.update(movie, info=[])

    return movies

def getBestMovie():
    top = ia.get_top250_movies()
    for movie in top:
        ia.update(movie, info=[])
    return top

def getMoviewithID(id):
    movie = ia.get_movie(id)
    return movie

def getCategory(movie):
    for item in movie['genres']:
        return item
    
def getRating(movie):
    return movie['rating']

def getlength(movie):
    return movie['runtime']

def getCast(movie):
   for item in movie['cast']:
        return item

def getLanguage(movie):
    for item in movie['languages']:
        return item


def getDate(movie):
        return movie['year']


def getimdbID(movie):
    return movie['imdbID']


def getTitle(movie):
    return movie['title']


def getDesc(movie):
    return movie['plot']


def getScreenshots(movie):
    for item in movie['screenshots']:
        return item

def getImage(movie):
    return movie['cover url']