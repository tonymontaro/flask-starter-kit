"""Application entry point."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()

from config import app_config
from app.api.routes import api_bp
from app.auth.routes import auth_bp


def create_app(env):
    """Configure and create flask app."""
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET') or 'a-very-long-string'
    app.config.from_object(app_config[env])
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp, url_prefix='/users')

    return app


app = create_app(os.getenv('ENV', 'development'))
