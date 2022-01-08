import os
from flask import Flask
from flask_pymongo  import PyMongo

# Config flask/mongodn locahost
app = Flask(__name__)
app.secret_key = os.urandom(24)
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/test")
MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY", "")

# Config connect with Mongodb
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

from app import routes