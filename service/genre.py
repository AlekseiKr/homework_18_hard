# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.genre import GenreDAO

class GenreService:

    def __init__(self, dao: GenreDAO):

        self.dao = dao

    def get_one(self, gid):

        return self.dao.get_one(gid)

    def get_all(self):

        return self.dao.get_all()