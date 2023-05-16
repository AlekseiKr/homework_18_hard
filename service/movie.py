# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie import MovieDAO

class MovieService:

    def __init__(self, dao: MovieDAO):

        self.dao = dao

    def get_one(self, mid):

        return self.dao.get_one(mid)

    def get_all(self):

        return self.dao.get_all()

    def get_by_director(self, director_id):

        return self.dao.get_by_director(director_id)

    def get_by_genre(self, genre_id):

        return self.dao.get_by_genre(genre_id)

    def get_by_year(self, year):

        return self.dao.get_by_year(year)
    def create(self, data):

        return self.dao.create(data)
    
    def update(self, data):
        
        mid = data.get("id")

        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director = data.get("director")

        self.dao.update(movie)

    def delete(self, mid):

        self.dao.delete(mid)
