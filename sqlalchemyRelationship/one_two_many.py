# coding: UTF-8
from flask import Flask
from flask_migrate import Migrate,  MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dba:111@45.78.9.17:3306/wq_01'
db = SQLAlchemy(app)





class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20)),
    age = db.Column(db.Integer),
    hobby = db.Column(db.String(20)),
    pets = db.relationship("Pet", backref=db.backref('owner', lazy='dynamic'))


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey("person.id"))


# from one_two_many import db
# db.create_all()


# from one_to_may import Person,Pet

# 如果我们在Person 中指定pets 的backref 为owner ，那么pet会自动添加一个属性owner  ,
# spot = Pet(name='Spot',owner=anthony)
# db.session.add(spot)
# db.session.commit()

Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if '__main__' == __name__:
    manager.run()
