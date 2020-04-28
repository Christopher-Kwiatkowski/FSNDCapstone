import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from models import db_drop_and_create_all, setup_db, Movie, Actor
from auth import AuthError, requires_auth

# except Exception as error:
#     print("Oops! An exception has occured:", error)
#     print("Exception TYPE:", type(error))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # db_drop_and_create_all()

    @app.after_request
    def after_request(response):
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-All-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('actors', methods=['GET'])
    @requires_auth("get:actors")
    def get_all_actors(jwt):
        try:
            actors = Actor.query.all()
            all_actors = [actor.format() for actor in actors]
            return jsonify({
                "success": True,
                "actors": all_actors
            })
        except:
            abort(401)

    @app.route('movies', methods=['GET'])
    @requires_auth("get:movies")
    def get_all_movies(jwt):
        try:
            movies = Movie.query.all()
            all_movies = [movie.format() for movie in movies]
            return jsonify({
                "success": True,
                "movies": all_movies
            })
        except:
            abort(401)

    @app.route('actors', methods=["POST"])
    @requires_auth("post:actors")
    def add_new_actor(jwt):
        try:
            new_actor = json.loads(request.data)
            name = new_actor['name']
            age = new_actor['age']
            gender = new_actor['gender']
            actor = Actor(name=name, age=age, gender=gender)
            array_of_actor = []
            array_of_actor.append(
                {'name': name, 'age': age, 'gender': gender})
            actor.insert()
            return jsonify({
                'success': True,
                'actors': array_of_actor
            })
        except:
            abort(400)

    @app.route('movies', methods=["POST"])
    @requires_auth("post:movies")
    def add_new_movie(jwt):
        try:
            new_movie = json.loads(request.data)
            title = new_movie['title']
            release = new_movie['release']
            movie = Movie(title=title, release=release)
            array_of_movie = []
            array_of_movie.append({'title': title, 'release': release})
            movie.insert()
            return jsonify({
                'success': True,
                'actors': array_of_movie
            })
        except:
            abort(400)

    @app.route('actors/<int:actor_id>', methods=["PATCH"])
    @requires_auth("patch:actors")
    def update_actor(jwt, actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if not actor:
                abort(404)
            update_to_actor = json.loads(request.data)
            if hasattr('update_to_actor', 'name'):
                actor.name = update_to_actor['name']
            if hasattr('update_to_actor', 'age'):
                actor.age = update_to_actor['age']
            if hasattr('update_to_actor', 'gender'):
                actor.gender = update_to_actor['gender']
            updated_actor = [
                {'id': actor.id, 'name': actor.name, 'age': actor.age, 'gender': actor.gender}]
            actor.update()
            return jsonify({
                'success': True,
                'actors': updated_actor
            })
        except:
            abort(404)

    @app.route('movies/<int:movie_id>', methods=["PATCH"])
    @requires_auth("patch:movies")
    def update_movie(jwt, movie_id):
        try:
            try:
                movie = Movie.query.get(movie_id)
            except:
                abort(404)
            update_to_movie = json.loads(request.data)
            if hasattr('update_to_movie', 'title'):
                movie.title = update_to_movie['title']
            if hasattr('update_to_movie', 'release'):
                movie.release = update_to_movie['release']
            updated_movie = [
                {'id': movie.id, 'title': movie.title, 'release': movie.release}]
            movie.update()
            return jsonify({
                'success': True,
                'movies': updated_movie
            })
        except:
            abort(404)

    @app.route('actors/<int:actor_id>', methods=["Delete"])
    @requires_auth("delete:actors")
    def delete_actor(jwt, actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if not actor:
                abort(404)
            actor_id = actor.id
            actor.delete
            return jsonify({
                'success': True,
                'actors': actor_id
            })
        except:
            abort(401)

    @app.route('movies/<int:movie_id>', methods=["Delete"])
    @requires_auth("delete:movies")
    def delete_movie(jwt, movie_id):
        try:
            movie = Movie.query.get(movie_id)
            if not movie:
                abort(404)
            movie_id = movie.id
            movie.delete
            return jsonify({
                'success': True,
                'movies': movie_id
            })
        except:
            abort(401)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        error_code = error.status_code
        description = error.error
        return jsonify({
            "success": False,
            "error": error_code,
            "message": description
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
