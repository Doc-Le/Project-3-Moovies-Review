import logging
from app import (app, mongo)
from flask import render_template

@app.route("/")
def main_page():
    movies = mongo.db.movies.find({"year": 2021})
    logging.info(movies)
    return render_template("index.html", movies=movies)