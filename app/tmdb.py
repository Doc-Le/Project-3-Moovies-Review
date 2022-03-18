from . import MOVIE_API_KEY
import tmdbsimple as tmdb
from .db import (get_movie_reviews_count, get_movie_reviews_average,)
from datetime import datetime
from .models import (
    Movie
)

tmdb.API_KEY = MOVIE_API_KEY
tmdb.REQUESTS_TIMEOUT = (2, 5)


def search_movies(query):
    """ search movie in api """
    search = tmdb.Search()
    search.movie(query=query)
    results = []
    for movie in search.results:
        movie_details = parse_movie(movie)
        results.append(movie_details)
    return results


def get_movie(id):
    """ search movie in api """
    movie = tmdb.Movies(id)
    movie_details = movie.info()
    return parse_movie(movie_details)


def parse_movie(movie):
    movie_id = movie["id"]
    year = 'N/A'
    if "release_date" in movie:
        year = movie["release_date"][0:4]
    rate_average = get_movie_reviews_average(movie_id)
    rate_count = get_movie_reviews_count(movie_id)
    return Movie(
        id=int(movie_id),
        title=movie["title"],
        overview=movie["overview"],
        backdrop_path=movie["backdrop_path"],
        poster_path=movie["poster_path"],
        year=year,
        rate_average=rate_average,
        rate_count=rate_count,
    )
