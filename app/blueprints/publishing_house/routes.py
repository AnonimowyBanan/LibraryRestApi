from flask import jsonify, request


from . import publishing_house
from app.extensions import db
from app.models import PublishingHouse


@publishing_house.route('/')
def get() -> jsonify:

    publishing_houses = PublishingHouse.query.all()

    return jsonify([publishing_house.to_dict() for publishing_house in publishing_houses]), 200


@publishing_house.route('/<int:publishing_house_id>')
def get_by_id(publishing_house_id: int) -> jsonify:

    publishing_house = PublishingHouse.query.get(publishing_house_id)

    return jsonify(publishing_house.to_dict()), 200


@publishing_house.route('/', methods=['POST'])
def create() -> jsonify:

    data = request.json
    publishing_house = PublishingHouse(data.get('name'), data.get('description'))

    db.session.add(publishing_house)
    db.session.commit()

    return jsonify(publishing_house.to_dict()), 201


@publishing_house.route('/<int:publishing_house_id>', methods=['PUT'])
def update(publishing_house_id: int) -> jsonify:

    publishing_house = PublishingHouse.query.get(publishing_house_id)

    data = request.json
    publishing_house.name = data.get('name', publishing_house.name)
    publishing_house.description = data.get('description', publishing_house.description)

    db.session.commit()

    return jsonify(publishing_house.to_dict()), 201


@publishing_house.route('/<int:publishing_house_id>', methods=['DELETE'])
def delete(publishing_house_id: int) -> jsonify:

    publishing_house = PublishingHouse.query.get(publishing_house_id)

    db.session.delete(publishing_house)
    db.session.commit()

    return jsonify(publishing_house.to_dict()), 200
