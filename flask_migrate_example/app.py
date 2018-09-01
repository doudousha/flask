from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dba:111@45.78.9.17:3306/wq_01'

db = SQLAlchemy(app)
Migrate(app, db) # 初始化migrate 上下文 ,这些参数被传递给Alembic的EnvironmentContext.configure()方法

manager = Manager(app)
manager.add_command("db", MigrateCommand)


class Student(db.Model):
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(20))
    age = db.Column('age', db.Integer)
    hobby = db.Column('hobby', db.String(126))
    aliasName = db.Column('alias_name', db.String(20))
    gender = db.Column('gender', db.String(12))


if __name__ == '__main__':
    manager.run()
