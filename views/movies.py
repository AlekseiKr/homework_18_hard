from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):

        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')

        if director is not None:

            all_movies = movie_service.get_by_director(director)

        elif genre is not None:

            all_movies = movie_service.get_by_genre(genre)

        elif year is not None:

            all_movies = movie_service.get_by_year(year)

        else:

            all_movies = movie_service.get_all()

        return movies_schema.dump(all_movies)

    def post(self):

        req_json = request.json
        movie_service.create(req_json)

        return "", 201

    @movie_ns.route('/<int:mid>')
    class MovieView(Resource):
        def get(self, mid:int):

            try:

                movie = movie_service.get_one(mid)

                return movie_schema.dump(movie), 200

            except Exception as e:
                return str(e), 404

        def put(self, mid):

            req_json = request.json
            req_json["id"] = mid

            movie_service.update(req_json)

            return "", 204

        def delete(self, mid: int):

            movie = movie_service.delete(mid)

            return "", 204


