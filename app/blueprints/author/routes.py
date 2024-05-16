from flask import jsonify, request

from . import author
from app.extensions import db
from app.models import Author


@author.route('/')
def get() -> jsonify:
    authors = db.session.execute(db.select(Author)).scalars()

    return jsonify([author.to_dict() for author in authors])


@author.route('/<int:author_id>')
def get_by_id(author_id) -> jsonify:
    author = db.session.execute(db.select(Author).filter_by(id=author_id)).scalar_one()

    return jsonify(author.to_dict())


@author.route('/', methods=['POST'])
def create() -> jsonify:
    data = request.get_json()

    author = Author(first_name=data.get('first_name'), last_name=data.get('last_name'), biography=data.get('biography'))

    db.session.add(author)
    db.session.commit()

    return jsonify(author.to_dict()), 201


@author.route('/<int:author_id>', methods=['PUT'])
def update(author_id) -> jsonify:
    data = request.get_json()

    author = db.session.execute(db.select(Author).filter_by(id=author_id)).scalar_one()

    author.first_name = data.get('first_name', author.first_name)
    author.last_name = data.get('last_name', author.last_name)
    author.biography = data.get('biography', author.biography)

    db.session.commit()

    return jsonify(author.to_dict()), 201


@author.route('/<int:author_id>', methods=['DELETE'])
def delete(author_id) -> jsonify:
    author = db.session.execute(db.select(Author).filter_by(id=author_id)).scalar_one()

    db.session.delete(author)
    db.session.commit()

    return jsonify(author.to_dict()), 200
