# TODO: Feature 3

from src.models.movie import Movie
from src.repositories.movie_repository import  get_movie_repository
def test_get_movie_by_title():
    
   
    movie_ex = ('Star Wars', 'George Lucas', 5)
    test = get_movie_repository.MovieRepository
    test.createMovie('Star Wars', 'George Lucas', 5)
    stored_movie = _movie_repo.get_movie_by_title("Star Wars")
    print(stored_movie)
    assert "Star Wars" == stored_movie.title
    
