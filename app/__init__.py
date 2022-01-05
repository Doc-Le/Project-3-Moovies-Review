import os
from flask import Flask
from flask_pymongo  import PyMongo
# from tmdb import create_session

app = Flask(__name__)
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/test")

MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY", "key")

# comments about mongodb connect
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

# comments about movie external api connect
# create_session(API_KEY)
#  import tmdb.py

from app import home
