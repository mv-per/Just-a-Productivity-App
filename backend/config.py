"""
This file contains most of the configuration variables that your app needs.
"""

import os

basedir = os.path.join(
    os.path.abspath(os.path.abspath(os.path.dirname(__file__))), "database"
)


# example to add additional configuration
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite'


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    # 'production': ProductionConfig,
    "default": DevelopmentConfig,
}
