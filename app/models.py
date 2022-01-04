class User:
  def __init__(self, username, password, authenticated):
    self.username = username
    self.password = password
    self.authenticated = authenticated

class Movie:
  def __init__(self, id, title):
    self.id = id
    self.title = title

class Review:
  def __init__(self, username, movie_id, rate, comments):
    self.username = username
    self.movie_id = movie_id
    self.rate = rate
    self.comments = comments
