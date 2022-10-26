# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def list_movies_test():

    movie = movie_repository.get_all_movies()
    movie_repository.create_movie('Star Wars', 'George Lucas', 3)
    movie = movie_repository.get_all_movies()
    assert movie.title == "Star Wars"
    


    movie_repository.create_movie('Iron Man', 'Jon Favreau', 5)
    movie = movie_repository.get_all_movies()
    assert movie.title == "Iron Man"
    


    movie_repository.create_movie('MidSommar', 'Ari Aster', 5)
    movie = movie_repository.get_all_movies()
    assert movie.title == "MidSommar"
    