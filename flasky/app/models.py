from . import db


class Movie(db.Model):
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    title = db.Column('title', db.String(255))
