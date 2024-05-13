from flask import jsonify, request

from . import author
from app.extensions import db
from app.models import Author


@author.route('/')
def get():
    authors = Author.query.all()

    return jsonify([author.to_dict() for author in authors])


@author.route('/<int:author_id>')
def get_by_id(author_id):
    author = Author.query.get(author_id)

    return jsonify(author.to_dict())


@author.route('/', methods=['POST'])
def create():
    data = request.get_json()

    author = Author(first_name=data.get('first_name'), last_name=data.get('last_name'), biography=data.get('biography'))

    db.session.add(author)
    db.session.commit()

    return jsonify(author.to_dict()), 201


@author.route('/<int:author_id>', methods=['PUT'])
def update(author_id):
    data = request.get_json()

    author = Author.query.get(author_id)

    author.first_name = data.get('first_name', author.first_name)
    author.last_name = data.get('last_name', author.last_name)
    author.biography = data.get('biography', author.biography)

    db.session.commit()

    return jsonify(author.to_dict()), 201


@author.route('/<int:author_id>', methods=['DELETE'])
def delete(author_id):
    author = Author.query.get(author_id)

    db.session.delete(author)
    db.session.commit()

    return jsonify(author.to_dict()), 200
