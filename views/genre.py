from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):

    def get(self):

        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres)

    @genre_ns.route('/<int:gid>')
    class GenreView(Resource):
        def get(self, gid:int):

            try:

                genre = genre_service.get_one(gid)

                return genre_schema.dump(genre), 200

            except Exception as e:
                return str(e), 404
