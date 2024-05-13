from flask import Flask
from .extensions import db
from .config import *
from .models import *
from .blueprints import *


def create_app(config_object: object):
    flask = Flask(__name__)

    flask.config.from_object(config_object)

    db.init_app(flask)

    with flask.app_context():
        db.create_all()

    flask.register_blueprint(app_bp)
    flask.register_blueprint(author_bp)
    flask.register_blueprint(book_bp)
    flask.register_blueprint(category_bp)
    flask.register_blueprint(publishing_house_bp)

    return flask


app = create_app(DevelopmentConfig)
