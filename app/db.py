

from app import (app, mongo)

""" 
Get user 
"""
def get_user(username):
    return mongo.db.users.find_one({ "username": username })

""" 
Authenticate user
"""
def authenticate_user(username, password):
    return bool(mongo.db.users.find({ "username": username, "password": password }).count() > 0)

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
    mongo.db.users.delete_one({ "username": username })


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
    return mongo.db.reviews.find_one({ "id": id })

""" 
Get movie reviews
"""
def get_movie_reviews(movie_id):
    return mongo.db.reviews.find({ "movie_id": movie_id })

""" 
Get user reviews
"""
def get_user_reviews(username):
    return mongo.db.reviews.find({ "username": username })

""" 
Insert review
"""
def insert_review(movie_id, username, rate):
    review = get_review_json(movie_id, username, rate)
    mongo.db.reviews.insert_one(review)

""" 
Update review
"""
def update_review(id, rate):
    old_review = get_review(id)
    review = { "id": id, "rate" : rate }
    mongo.db.reviews.update_one(old_review, review)

""" 
Delete review
"""
def delete_review(id):
    mongo.db.reviews.delete_one({ "id": id })

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
        "movie_id" : movie_id,
        "username" : username, 
        "rate" : rate
    }