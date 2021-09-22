# import os
from flask import Flask
# from flask_pymongo  import PyMongo

app = Flask(__name__)
# app.config['MONGO_URI'] = IP = os.environ.get("MONGO_URI", "mongodb://localhost:27017/test")

# mongo = PyMongo(app)

from app import home
# from app import api
