import os


class Config(object):
    """Base config."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "uhJNH45a57aH5MNccs567894sdsds45sff"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    SERVER_NAME = '0.0.0.0:5000'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_FOLDER = os.path.join('app', 'db')
    DB_FILE = "development-db.db"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_FOLDER, DB_FILE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = False



class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False

