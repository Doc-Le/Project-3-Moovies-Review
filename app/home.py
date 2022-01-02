import logging
from app import (app, mongo)
from app import app
from flask import render_template

@app.route("/")
def main_page():
    return render_template("index.html", movies=[])

@app.route("/movies")
def get_movies():
    cursor = mongo.db.movies.find()
    movies = [doc.to_json() for doc in cursor]
    return {
        "movies": movies,
    }