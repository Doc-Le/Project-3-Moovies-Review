
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

"""
class Movie(JsonSerializable):
  def __init__(
    self, 
    id,
    title,
    overview,
    backdrop_path,
    poster_path,
    year,
    rate_average,
    rate_count,
  ):
    self.id = id
    self.title = title
    self.overview = overview
    self.backdrop_path = backdrop_path
    self.poster_path = poster_path
    self.year = year
    self.rate_average = rate_average
    self.rate_count = rate_count

class Review(JsonSerializable):
  def __init__(self, id, username, movie_id, rate, comments):
    self.id = id
    self.review_id = "{}_{}".format(movie_id, username)
    self.username = username
    self.movie_id = movie_id
    self.rate = rate


"""
Redirect request model
"""
class UrlRedirect:
  def __init__(self, request):
    self.to = request.args.get("red_url")
    if self.to != None:
      self.params = "?red_url={}".format(self.to)
    else:
      self.params = ""
  def __str__(self):
        return self.to