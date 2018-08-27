from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dba:111@45.78.9.17:3306/wq_01'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    pets = db.relationship("Pet", backref=db.backref('owner', lazy='dynamic'))


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey("person.id"))

# from one_two_many import db
# db.create_all()


# from one_to_may import Person,Pet

# spot = Pet(name='Spot',owner=anthony)
# db.session.add(spot)
# db.session.commit()
