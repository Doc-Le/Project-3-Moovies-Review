class User:
  def __init__(self, username, password, authenticated):
    self.username = username
    self.password = password
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
class Movie:
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
    vote_coun,
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

class Review:
  def __init__(self, username, movie_id, rate, comments):
    self.username = username
    self.movie_id = movie_id
    self.rate = rate
    self.comments = comments
