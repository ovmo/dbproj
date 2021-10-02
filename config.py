import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DEBUG = os.getenv('DEBUG_MODE',False)
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = SECRET_KEY

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    engine = create_engine('mysql://' + DB_USER + ':' + DB_PASS + '@localhost/' + DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@localhost/' + DB_NAME

    Session = sessionmaker(bind=engine)


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
