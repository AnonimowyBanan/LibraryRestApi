from flask import Blueprint

publishing_house = Blueprint('publishing_house', __name__, url_prefix='/publishing-house')

from . import routes