from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.config import app_config
from app.api import routes as api_routes


def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[env])
    db.init_app(app)

    api = Api(app)
    api.add_resource(api_routes.Home, '/')

    return app
