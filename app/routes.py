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
from .tmdb import (
    search_movies
)
from .utils import (
    get_user_session,
    clear_user_session,
)

## root api direct to index.html (home page)

@app.route("/", methods = ["GET"])
def index():
    context = {
        "title": "",
        "user": get_user_session(),
        "show_signup": False,
        "show_header_search": False
    }
    return render_template("index.html", context=context)

@app.route("/search", methods = ["POST"])
def search():
    movies = []
    query = request.form["query"]
    movies = search_movies(query)
    # extract movie id list to search reviews in mongodb
    # reviews = mongo.db.reviews.find({})
    context = {
        "title": "Result",
        "user": get_user_session(),
        "movies": movies,
        "show_header_search": True
    }
    return render_template("search_result.html", context=context)

@app.route("/profile/<username>", methods = ["GET", "POST", "PUT", "DELETE"])
def profile(username):
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

    context = {
        "title": "Profile",
        "user": get_user_session(),
        "show_header_search": True,
        "method": method
    }

    # check if user is logged in   
    # set user session
    return render_template("profile.html", context=context)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    show_message = False
    method = request.method
    message = "Success registered user!"
    if method == "POST":
        if request.form.get("password") == request.form.get("repeat-password"):
            username = request.form.get("username")
            password = request.form.get("password")
            # create user mongodb
            show_message = True            
        else:
            message = "Both passwords must be equal!"
            show_message = True
    
    context = {
        "title": "Sign-up",
        "user": get_user_session(),
        "show_header_search": True,
        "show_message": show_message,
        "message": message,
        "method": method
    }
    return render_template("signup.html", context=context)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Success logged in!"
    method = request.method
    if method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # consult mongodb for user data
        # create user session
        # set user object
    context = {
        "title": "Login",
        "user": get_user_session(),
        "show_header_search": True,
        "message": message,
        "method": method
    }
    return render_template("login.html", context=context)    

@app.route("/logout")
def logout():
    context = {
        "title": "",
        "user": clear_user_session(),
        "show_header_search": False
    }
    return render_template("index.html", context=context)

"""
Authentication required
User needs to sign-up and login to review
"""
@app.route("/reviews/<id>", methods = ["GET", "POST", "PUT", "DELETE"])
def review(id):
    method = request.method
    subtitle = "Review form"

    # """return the information for <user_id>"""
    # if user.authenticated not True:
    #   method = ""
    #   context = {
    #       "title": "",
    #       "user": get_user_session(),
    #       "show_signup": True,
    #       "show_header_search": False
    #   }
    #   return render_template("login.html", context=context)
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
        """return movie review form"""

    context = {
        "title": "Review",
        "subtitle": subtitle,
        "user": get_user_session(),
        "show_header_search": True,
        "method": method
    }

    # check if user is logged in
    # set user session
    return render_template("review.html", context=context)
