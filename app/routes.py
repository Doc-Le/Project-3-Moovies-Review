import json
import logging

from . import MOVIE_API_KEY
from bson import json_util
from app import (app, mongo)
from app import app
from bson.objectid import ObjectId
from flask import request, render_template, redirect
from .db import (
    get_movie_user_review, get_user, insert_review,
    insert_user, authenticate_user, update_review)
from .models import (User, Movie, Review, UrlRedirect)
from .tmdb import (search_movies, get_movie)
from .utils import (
    set_user_session, get_user_session,
    clear_user_session, is_authenticated)


@app.route("/", methods=["GET"])
def index():
    context = {
        "title": "",
        "user": get_user_session(),
        "show_signup": False,
        "show_header_search": False
    }
    return render_template("index.html", context=context)


@app.route("/search", methods=["POST"])
def search():
    query = None
    movies = []

    if request.form.get("query", None):
        query = request.form["query"]
    elif request.form.get("query_header", None):
        query = request.form["query_header"]

    if query != None:
        movies = search_movies(query)

    context = {
        "title": "Result",
        "user": get_user_session(),
        "query": query,
        "movies": movies,
        "show_header_search": True
    }
    return render_template("search_result.html", context=context)


@app.route("/profile/<username>", methods=["GET", "POST", "PUT", "DELETE"])
def profile(username):
    method = request.method

    # Check if user authenticated otherwise redirect to login
    if is_authenticated():
        return redirect("/login?red_url={}".format(request.path), code=302)

    if method == "POST":
        """return the information for <user_id>"""
        # request.form["username"]
        # request.form["password"]

    if method == "PUT":
        """return the information for <user_id>"""

    if method == "DELETE":
        """return the information for <user_id>"""

    else:  # GET
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
    url_redirect = UrlRedirect(request)
    message = ""
    show_message = False
    username_exist = False

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if get_user(username) != None:
            # Validate username already exists
            message = "Username {} already exist. Please, choose different one".format(username)
            username_exist = True
            show_message = False
        else:
            # return message to make sure both passwords are equal
            user = {"username": username, "password": password}
            insert_user(user)
            message = "Success registered user {}!".format(username)
            show_message = True

    context = {
        "title": "Sign-up",
        "user": get_user_session(),
        "url_redirect": url_redirect,
        "username_exist": username_exist,
        "show_header_search": True,
        "show_message": show_message,
        "message": message
    }
    return render_template("signup.html", context=context)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Success logged in!"
    show_message = False
    show_form = True
    url_redirect = UrlRedirect(request)
    show_signup = bool(url_redirect != None)

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
            if url_redirect.to != None:
                return redirect(url_redirect.to, code=302)
            else:
                message = "You are logged in {}!".format(username)
                show_message = True
                show_form = False

    context = {
        "title": "Login",
        "user": get_user_session(),
        "url_redirect": url_redirect,
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


@app.route("/reviews/<id>", methods=["GET", "POST", "PUT", "DELETE"])
def review(id):
    message = ""
    user = get_user_session()
    username = user["username"]
    movie = get_movie(int(id))
    review = get_movie_user_review(id, username)
    rate = 0

    # Check if user authenticated otherwise redirect to login
    if is_authenticated():
        return redirect("/login?red_url={}".format(request.path), code=302)

    if review != None:
        rate = review["rate"]

    if request.method == "POST":
        rate = float(request.form["options"])
        if review != None:
            update_review(review["id"], rate)
            message = "Thanks for updating your previous review this movie!"
        else:
            insert_review(id, username, rate)
            message = "Thanks for reviewing this movie!"
        movie = get_movie(int(id))

    context = {
        "title": "Review",
        "user": get_user_session(),
        "movie": movie,
        "rate": int(rate),
        "show_header_search": True,
        "message": message
    }

    # check if user is logged in
    # set user session
    return render_template("review.html", context=context)
