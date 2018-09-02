import os
from builtins import staticmethod


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wq_02:111@45.78.9.17:3306/wq_02?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wq_02:111@45.78.9.17:3306/wq_02?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


cfxConfig = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
