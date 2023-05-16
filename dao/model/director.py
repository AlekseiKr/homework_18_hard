from setup_db import db
from marshmallow import Schema, fields

class Director(db.Model):

    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    movies = db.relationship('Movie', back_populates = 'director')

class DirectorSchema(Schema):

    id = fields.Int()
    name = fields.Str()

