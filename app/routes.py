import json
import logging

from . import MOVIE_API_KEY
from bson import json_util
from app import (app, mongo)
from app import app
from bson.objectid import ObjectId
from flask import request, render_template, session, redirect
from .db import (get_user,insert_user,authenticate_user)
from .models import (User, Movie, Review)
from .tmdb import (search_movies)
from .utils import (set_user_session, get_user_session, clear_user_session, is_authenticated)

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
    
    # Check if user authenticated otherwise redirect to login
    if is_authenticated():
       return redirect("/login?red_url={}".format(request.path),code=302)

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
    message = ""
    show_message = False
    username_exist = False

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repeatPassword = request.form.get("repeat-password")

        if get_user(username) != None:
            # Validate username already exists
            message = "Username {} already exist. Please, choose another username".format(username)
            username_exist = True
            show_message = False
        else:
            # return message to make sure both passwords are equal
            user = { "username": username, "password": password }
            insert_user(user)
            message = "Success registered user!"
            show_message = True

    context = {
        "title": "Sign-up",
        "user": get_user_session(),
        "username_exist": username_exist,
        "show_header_search": True,
        "show_message": show_message,
        "message": message
    }
    return render_template("signup.html", context=context)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Success logged in!"
    show_signup = False
    show_message = False
    show_form = True
    redirect_to = request.args.get("red_url")
    redirect_form = ""

    if redirect_to != None:
        show_signup = True
        redirect_form = "?red_url={}".format(redirect_to)

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        authenticated = authenticate_user(username=username, password=password)
        if authenticated != True:
           message = "Username or Password incorrect. Please try again!"
           show_message = True
           show_form = True
        else:
           set_user_session(username=username, authenticated=authenticated)
           if redirect_to != None:
                return redirect(redirect_to,code=302)  
           else:
                message = "Success logged in with username {}!".format(username)
                show_message = True
                show_form = False

    context = {
        "title": "Login",
        "user": get_user_session(),
        "redirect_form": redirect_form,
        "show_header_search": True,
        "show_signup": show_signup,
        "show_message": show_message,
        "show_form": show_form,
        "message": message
    }
    return render_template("login.html", context=context)    

@app.route("/logout")
def logout():
    clear_user_session()
    context = {
        "title": "",
        "user": get_user_session(),
        "show_header_search": False
    }
    return render_template("index.html", context=context)

@app.route("/reviews/<id>", methods = ["GET", "POST", "PUT", "DELETE"])
def review(id):
    method = request.method
    subtitle = "Review form"
    user = get_user_session()

    # Check if user authenticated otherwise redirect to login
    if is_authenticated():
       return redirect("/login?red_url={}".format(request.path),code=302)

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
