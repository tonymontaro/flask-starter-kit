"""Configuration file."""
import os
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))


class Config(object):
    """Default configuration."""

    DEBUG = False
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = (os.getenv('DATABASE_URL') or
                               'sqlite:///' + join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    """Development configuration."""

    DEBUG = True


class Testing(Config):
    """Test configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.getenv('DATABASE_TEST_URL') or
                               'sqlite:///' + join(basedir, 'test.db'))


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Config
}
