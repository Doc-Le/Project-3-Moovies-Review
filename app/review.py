from app import (mongo)


def get_movie_review(movie_id):
    # get review in mongodb collection review
    # if review exist then return review parsed
    # if review does not exist then return new review empty
    return reviews

def set_movie_review(movie_id, review):
    # add new movie review in mongodb collection review
    return review



# def get_review(movie_id):
#     return mongo.db.reviews.find_one({ "movie_id": movie_id })
# def add_review(movie_id, review):
# def update_review(movie_id, review):
# def delete_review(movie_id, review):
#     # add new movie review in mongodb collection review
#     return review