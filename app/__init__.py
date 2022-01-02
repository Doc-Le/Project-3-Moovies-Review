import os
from flask import Flask
from flask_pymongo  import PyMongo

app = Flask(__name__)
MONGO_URI = os.environ.get("MONGO_URI")
print(MONGO_URI)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

from app import home
# from app import api
