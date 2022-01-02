import json
import logging

from bson import json_util
from app import (app, mongo)
from app import app
from bson.objectid import ObjectId
from flask import render_template

@app.route("/")
def main_page():
    movies = mongo.db.movies.find()
    return render_template("index.html", movies=movies)

@app.route("/movies")
def get_movies():
    cursor = mongo.db.movies.find()
    movies = json.loads(json_util.dumps(cursor))
    return {
        "movies": movies,
    }

@app.route("/movies/<id>")
def get_movie_id(id):
    cursor = mongo.db.movies.find_one({ "_id": ObjectId(id) })
    movie = json.loads(json_util.dumps(cursor))
    return {
        "movie": movie,
    }