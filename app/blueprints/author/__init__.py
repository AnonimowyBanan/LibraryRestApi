from flask import Blueprint

author = Blueprint('author', __name__, url_prefix='/author')

from . import routes
