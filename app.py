# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.genre import genre_ns
from views.director import director_ns


# функция создания основного объекта app
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application
def configure_app(application: Flask):

    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def load_data():

    db.create_all()
    db.session.commit()

if __name__ == '__main__':

    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()