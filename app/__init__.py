"""Application entry point."""
import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()

from app.config import app_config
from app.api import routes as api_routes
from app.auth import routes as auth_routes


def create_app(env):
    """Configure and create flask app."""
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET') or 'averylongword'
    app.config.from_object(app_config[env])
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    api = Api(app)
    api.add_resource(api_routes.Home, '/')
    api.add_resource(api_routes.Protected, '/protected')

    api.add_resource(auth_routes.Register, '/register')
    api.add_resource(auth_routes.Login, '/login')
    api.add_resource(auth_routes.Logout, '/logout')

    return app
