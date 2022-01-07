import os
from flask import Flask
from flask_pymongo  import PyMongo


app = Flask(__name__)
app.secret_key = os.urandom(24)
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/test")
MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY", "30d7f1144aa1d0fce3d64afb43bb9a61")

# comments about mongodb connect
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

from app import routes