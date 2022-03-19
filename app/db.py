from pymongo import cursor
from .utils import process_cursor
from app import (app, mongo)

""" 
Get user 
"""


def get_user(username):
    return mongo.db.users.find_one({"username": username})


""" 
Authenticate user
"""


def authenticate_user(username, password):
    return bool(mongo.db.users.find({"username": username, "password": password}).count() > 0)


""" 
Insert user 
"""


def insert_user(user):
    mongo.db.users.insert_one(user)


""" 
Update user 
"""


def update_user(username, user):
    old_user = get_user(username)
    mongo.db.users.update_one(old_user, user)


""" 
Delete user 
"""


def delete_user(username):
    mongo.db.users.delete_one({"username": username})


""" 
Get review
{
    "movie_id": 29142,
    "reviews": [
        {
            "username": "johndoe",
            "rate": 3
        }
    ]
}
"""


def get_review(id):
    return mongo.db.reviews.find_one({"id": id})


""" 
Get movie reviews
"""


def get_movie_reviews(movie_id):
    return mongo.db.reviews.find({"movie_id": movie_id})


""" 
Count movie reviews
"""


def get_movie_reviews_count(movie_id):
    movie_id = int(movie_id)
    cursor = get_movie_reviews(movie_id)
    reviews = process_cursor(cursor)
    return len(reviews)


""" 
Get movie reviews average
"""


def get_movie_reviews_average(movie_id):
    movie_id = int(movie_id)
    average = 0
    count = get_movie_reviews_count(movie_id)

    if count == 1:
        review = mongo.db.reviews.find_one({"movie_id": movie_id})
        if "rate" in review:
            average = float(review["rate"])
    else:
        # Example from : https://docs.mongodb.com/manual/reference/operator/aggregation/avg/#use-in--group-stage
        cursor = mongo.db.reviews.aggregate([
            {
                "$match": {
                    "movie_id": {
                        "$eq": movie_id
                    }
                }
            },
            {
                "$group": {
                    "_id": "$movie_id",
                    "average": {
                        "$avg": "$rate"
                    }
                }
            }
        ])
        result = process_cursor(cursor)
        if len(result) > 0:
            average = float("{0:.1f}".format(result[0]["average"]))
    return average


""" 
Get user movie review
"""


def get_movie_user_review(movie_id, username):
    movie_id = int(movie_id)
    return mongo.db.reviews.find_one({"movie_id": movie_id, "username": username})


""" 
Get user reviews
"""


def get_user_reviews(username):
    return mongo.db.reviews.find({"username": username})


""" 
Insert review
"""


def insert_review(movie_id, username, rate):
    review = get_review_json(int(movie_id), username, rate)
    mongo.db.reviews.insert_one(review)


""" 
Update review
"""


def update_review(id, rate):
    mongo.db.reviews.update_one({"id": id}, {"$set": {"rate": rate}})


""" 
Delete review
"""


def delete_review(id):
    mongo.db.reviews.delete_one({"id": id})


""" 
Generate unique id for review
"""


def get_review_id(movie_id, username):
    return "{}_{}".format(movie_id, username)


"""
Get JSON review object
"""


def get_review_json(movie_id, username, rate):
    id = get_review_id(movie_id, username)
    return {
        "id": id,
        "movie_id": movie_id,
        "username": username,
        "rate": rate
    }
