"""Configuration file."""
import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv

basedir = abspath(dirname(__file__))
load_dotenv(join(basedir, '.env'))


def get_sqlite_url(db_name):
    """Return an sqlite url"""
    return 'sqlite:///' + join(basedir, db_name)


class Config(object):
    """Default configuration."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
            os.getenv('DATABASE_URL') or get_sqlite_url('app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    """Development configuration."""

    DEBUG = True


class Testing(Config):
    """Test configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
            os.getenv('DATABASE_TEST_URL') or get_sqlite_url('test.db'))


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Config
}
