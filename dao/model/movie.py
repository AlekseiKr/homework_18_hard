from setup_db import db
from marshmallow import Schema, fields

class Movie(db.Model):

    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre', back_populates='movies')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director', back_populates='movies')

class MovieSchema(Schema):

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
