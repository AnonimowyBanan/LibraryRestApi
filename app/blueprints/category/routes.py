from flask import jsonify, abort, request

from . import category
from app.models import Category
from app.extensions import db


@category.route('/')
def get() -> jsonify:

    categories = Category.query.all()

    if not categories:
        abort(404, 'No categories found')

    return jsonify([category.to_dict() for category in categories]), 200


@category.route('/<int:category_id>')
def get_by_id(category_id: int) -> jsonify:

    category = Category.query.get(category_id)

    if not category:
        abort(404, 'No category found')

    return jsonify(category.to_dict()), 200


@category.route('/', methods=['POST'])
def create() -> jsonify:
    data = request.get_json()

    category = Category(name=data.get('name'), description=data.get('description'))

    db.session.add(category)
    db.session.commit()

    return jsonify(category.to_dict()), 201


@category.route('/<int:category_id>', methods=['PUT'])
def update(category_id: int) -> jsonify:
    data = request.get_json()

    category = Category.query.get(category_id)

    category.name = data.get('name', category.name)
    category.description = data.get('description', category.description)

    db.session.commit()

    return jsonify(category.to_dict()), 201


@category.route('/<int:category_id>', methods=['DELETE'])
def delete(category_id: int) -> jsonify:

        category = Category.query.get(category_id)

        if not category:
            abort(404, 'No category found')

        db.session.delete(category)
        db.session.commit()

        return jsonify({'message': 'Category deleted'}), 200
