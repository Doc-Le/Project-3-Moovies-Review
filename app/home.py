import logging
# from app import (app, mongo)
from app import app
from flask import render_template

@app.route("/")
def main_page():
    movies = mongo.db.movies.find({})
#     movies=[
#         { "name": "Movie 1", "year": 2018 },
#         { "name": "Movie 2", "year": 2019 },
#         { "name": "Movie 3", "year": 2020 },
#         { "name": "Movie 4", "year": 2021 }
#     ]
    logging.info(movies)
    return render_template("index.html", movies=movies)
