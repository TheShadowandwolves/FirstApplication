from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books():
    return render_template("Books.html")

app.run(debug=True)
