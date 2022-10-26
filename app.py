from urllib import request
from flask import Flask, redirect, render_template,request


from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)




movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1

    print(movie_repository.get_all_movies())
 
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie_repository.get_all_movies())

    






@app.get('/movies/new')
def create_movies_form():

    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    name = request.form.get('name')
    director = request.form.get('director')
    rating = request.form['rating']
    movie_repository.create_movie(name, director,rating)
    
    return redirect('/movies')
#create_movie()
#list_all_movies()


@app.get('/movies/search')
def search_movies():
    title = request.args.get('title')    
    search_result = movie_repository.get_movie_by_title(title) 
    return render_template('search_movies.html', search_active=True, search_result=search_result)
