from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import cfxConfig

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(cfxConfig[config_name])
    cfxConfig[config_name].init_app(app)

    db.init_app(app)
    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
