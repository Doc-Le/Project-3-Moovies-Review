from . import MOVIE_API_KEY
import tmdbsimple as tmdb
from .models import (
    Movie
)

tmdb.API_KEY = MOVIE_API_KEY
tmdb.REQUESTS_TIMEOUT = (2, 5)

def search_movies(query):
    """ search movie in api """ 
    search = tmdb.Search()
    response = search.movie(query=query)
    return search.results

def get_movie(id):
    """ search movie in api """
    movie = tmdb.Movies(id)
    return movie.info()