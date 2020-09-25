import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actors, Movies

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # GET /actors and /movies

  @app.route('/actors')
  def get_all_actors():
    all_actors = Actors.query.all()

    return jsonify({
      'success': True,
      'movies': all_actors
    })
  
  @app.route('/movies')
  def get_all_movies():
    all_movies = Movies.query.all()

    return jsonify({
      'success': True,
      'movies': all_movies
    })


  # DELETE /actors/ and /movies/
  # POST /actors and /movies and
  # PATCH /actors/ and /movies/

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)