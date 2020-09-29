import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import setup_db, Actors, Movies
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/actors')
  @requires_auth('get:actors')
  def get_all_actors(payload):
    all_actors_query = Actors.query.all()
    all_actors = []
    for actor in all_actors_query:
      all_actors.append({
        'id': actor.id,
        'name': actor.name,
        'age': actor.age,
        'gender': actor.gender
      })      

    return jsonify({
      'success': True,
      'actors': all_actors
    })

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_all_movies(payload):
    all_movies_query = Movies.query.all()
    all_movies = []
    for movie in all_movies_query:
      all_movies.append({
        'id': movie.id,
        'title': movie.title,
        'releaseDate': movie.releaseDate,
      })
    
    return jsonify({
      'success': True,
      'movies': all_movies
    })


  # DELETE /actors/ and /movies/
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, id):
    try:
      actor_to_delete = Actors.query.get(id)
    except:
      abort(404)

    try:
      actor_to_delete.delete()

      return jsonify({
        "success": True,
        "delete": actor_to_delete.id
      })
    
    except:
      abort(422)

  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, id):
    
    try:
      movie_to_delete = Movies.query.get(id)
    except:
      abort(404)

    try:
      movie_to_delete.delete()

      return jsonify({
        "success": True,
        "delete": movie_to_delete.id
      })

    except:
      abort(422)

  # POST /actors and /movies
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_actor(payload):
    new_actor_info = request.get_json()

    if(new_actor_info is None):
      abort(422)
    
    name = new_actor_info.get('name')
    age = new_actor_info.get('age')
    gender = new_actor_info.get('gender')

    try:
      new_actor = Actors(name = name, age = age, gender = gender)
      new_actor.insert()
      
      return jsonify({
        'success': True,
        'actor': new_actor_info
      })
    
    except:
      abort(422)

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_movie(payload):
    new_movie_info = request.get_json()

    if(new_movie_info is None):
      abort(422)

    title = new_movie_info.get('title')
    releaseDate = new_movie_info.get('releaseDate')

    try:
      new_movie = Movies(title = title, releaseDate = releaseDate)
      new_movie.insert()

      return jsonify({
        'success': True,
        'movie': new_movie_info
    })

    except:
      abort(422)

    
  # PATCH /actors/ and /movies/
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actor(payload, id):
    
    edit_actor_info = request.get_json()

    if not edit_actor_info:
      abort(422)

    name = edit_actor_info.get('name')
    age = edit_actor_info.get('age')
    gender = edit_actor_info.get('gender')

    try:
      edit_actor_query = Actors.query.get(id)
    except:
      abort(404)
    
    try:
      if name:
        edit_actor_query.name = name

      if age:
        edit_actor_query.age = age
      
      if gender:
        edit_actor_query.gender = gender

      edit_actor_query.update()

      edited_actor = {
        'id': edit_actor_query.id,
        'name': edit_actor_query.name,
        'age': edit_actor_query.age,
        'gender': edit_actor_query.gender
      }

      return jsonify({
        "success": True,
        "actor": edited_actor
      })
    except:
      abort(422)

  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movie(payload, id):
    
    edit_movie_info = request.get_json()

    if not edit_movie_info:
      abort(422)

    title = edit_movie_info.get('name')
    releaseDate = edit_movie_info.get('releaseDate')

    try:
      edit_movie_query = Movies.query.get(id)
    except:
      abort(404)
    
    try:
      if title:
        edit_movie_query.title = title

      if releaseDate:
        edit_movie_query.releaseDate = releaseDate

      edit_movie_query.update()

      edited_movie = {
        'title': edit_movie_query.id,
        'releaseDate': edit_movie_query.releaseDate,
      }

      return jsonify({
        "success": True,
        "actor": edited_movie
      })
    except:
      abort(422)
  #Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "404 Not Found"
    }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "405 Method Not Allowed"
    }), 405

  @app.errorhandler(AuthError)
  def auth_error(ex):
    return jsonify({
      "success": False, 
      "error": 401,
      "message": ex.error
    }), 401
  
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)