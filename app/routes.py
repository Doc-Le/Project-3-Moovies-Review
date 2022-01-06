import json
import logging

from . import MOVIE_API_KEY
from bson import json_util
from app import (app, mongo)
from app import app
from bson.objectid import ObjectId
from flask import request, render_template, session
from .models import (
    User,
    Movie,
    Review
)
from .review import get_movie_review
from .tmdb import (
    search_movies
)

## root api direct to index.html (home page)

@app.route("/", methods = ["GET", "POST"])
def index():
    method = request.method
    movies = []
    search_result = False
    if method == "POST":
        """return the information for <user_id>"""
        query = request.form["query"]
        movies = search_movies(query)
        # extract movie id list to search reviews in mongodb
        # reviews = mongo.db.reviews.find({})
        search_result = True

    return render_template("index.html", movies=movies, search_result=search_result)

@app.route("/profile/<username>", methods = ["GET", "POST", "PUT", "DELETE"])
def profile(username):
    user = {}
    method = request.method
    # user = session["user"]

    # """return the information for <user_id>"""
    # if user.authenticated not True:
    #     method = ""
    #     return render_template("profile.html", user=user, method=method)
    print(request.form)

    if method == "POST":
        """return the information for <user_id>"""
        # request.form["username"]
        # request.form["password"]

    if method == "PUT":
        """return the information for <user_id>"""

    if method == "DELETE":
        """return the information for <user_id>"""

    else: # GET
        """return the information for <user_id>"""

    # check if user is logged in   
    # set user session
    return render_template("profile.html", user=user, method=method)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    show_message = False
    message = "Success registered user!"
    method = request.method
    if method == "POST":
        if request.form.get("password") == request.form.get("repeat-password"):
            username = request.form.get("username")
            password = request.form.get("password")
            # create user mongodb
            message = "Success registered user!"
            show_message = True            
        else:
            message = "Both passwords must be equal!"
            show_message = True
    return redirect("signup.html", message=message, show_message=show_message)

@app.route("/login", methods=["GET", "POST"])
def login():
    user = User(authenticated=False)
    message = "Success logged in!"
    method = request.method
    if method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # consult mongodb for user data
        # create user session
        # set user object

    return redirect("login.html", user=user, message=message)

@app.route("/logout")
def logout():
    """Shows the logout option"""
    message = "Logged out. Thanks for visiting Ratings!"
    # clear session["user_id"]
    user = None
    return redirect("index.html", user=user, message=message)

"""
Authentication required
User needs to sign-up and login to review
"""
@app.route("/reviews/<id>", methods = ["GET", "POST", "PUT", "DELETE"])
def review(id):
    user = User(username="", password="", authenticated=False)
    # movie = Movie(id)
    movie = {}
    method = request.method
    #user = (user_id=session)    # user = session["user"]

    # """return the information for <user_id>"""
    # if user.authenticated not True:
    #     method = ""
    #     return render_template("profile.html", user=user, method=method)
    print(request.form)

    if method == "POST":
        """return the information for <user_id>"""
        # request.form["username"]
        # request.form["password"]

    if method == "PUT":
        """return the information for <movie_id>"""

    if method == "DELETE":
        """return the information for <movie_id>"""

    else: # GET
        """return the information for <movie_id>"""

    # check if user is logged in
    # set user session
    return render_template("review.html", user=user, movie=movie, method=method)

def review_id(id):
    return mongo.db.reviews.find_one({ "_id": ObjectId(id) })

 #@app.route("/")
 #def main_page():
#     movies = mongo.db.movies.find()
#     return render_template("index.html", movies=movies)

# @app.route("/movies")
# def get_movies():
#     cursor = mongo.db.movies.find()
#     movies = json.loads(json_util.dumps(cursor))
#     return {
#         "movies": movies,
#     }

#@app.route("/movies/<id>", methods = ["GET", "POST", "PUT", "DELETE"])
  #def get_movie_id(id):
     # cursor = mongo.db.movies.find_one({ "_id": ObjectId(id) })
     # movie = json.loads(json_util.dumps(cursor))
     # return {
      ## "movie": movie,
    #}