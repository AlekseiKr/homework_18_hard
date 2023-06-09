# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.genre import Genre

class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, gid):

        return self.session.query(Genre).get(gid)

    def get_all(self):

        return self.session.query(Genre).all()



