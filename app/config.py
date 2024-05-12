class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
