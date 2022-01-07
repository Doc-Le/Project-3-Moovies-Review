
import json

"""
Json serializable class
Parse any object to JSON string
source: https://stackoverflow.com/a/11062658
"""
class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()

"""
User model inherets JsonSerializable class
"""
class User(JsonSerializable):
  def __init__(self, username, authenticated):
    self.username = username
    self.authenticated = authenticated

"""

{
  "adult": false,
  "backdrop_path": "/ymLLxJEm3HSM63A8lZ3oZAxiHR1.jpg",
  "genre_ids": [
      28,
      80,
      18,
      36,
      53
  ],
  "id": 29142,
  "original_language": "en",
  "original_title": "Executive Action",
  "overview": "Rogue intelligence agents, right-wing politicians, greedy capitalists, and free-lance assassins plot and carry out the JFK assassination in this speculative agitprop.",
  "popularity": 2.894,
  "poster_path": "/98G5HS7hU03wjiTjJ7SDuq20AHx.jpg",
  "release_date": "1973-11-07",
  "title": "Executive Action",
  "video": false,
  "vote_average": 6.4,
  "vote_count": 26
}
"""
class Movie(JsonSerializable):
  def __init__(
    self, 
    id,
    adult,
    backdrop_path,
    genre_ids,
    original_language,
    original_title,
    overview,
    popularity,
    poster_path,
    release_date,
    title,
    video,
    vote_average,
    vote_count,
    review
  ):
    self.id = id
    self.adult = adult
    self.backdrop_path = backdrop_path
    self.genre_ids = genre_ids
    self.original_language = original_language
    self.original_title = original_title
    self.overview = overview
    self.popularity = popularity
    self.poster_path = poster_path
    self.release_date = release_date
    self.title = title
    self.video = video
    self.vote_average = vote_average
    self.vote_count = vote_count
    self.review = review

class Review(JsonSerializable):
  def __init__(self, id, username, movie_id, rate, comments):
    self.id = id
    self.review_id = "{}_{}".format(movie_id, username)
    self.username = username
    self.movie_id = movie_id
    self.rate = rate
