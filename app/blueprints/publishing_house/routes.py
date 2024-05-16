from flask import jsonify, request


from . import publishing_house
from app.extensions import db
from app.models import PublishingHouse


@publishing_house.route('/')
def get() -> jsonify:

    publishing_houses = db.session.execute(db.select(PublishingHouse)).scalars()

    return jsonify([publishing_house.to_dict() for publishing_house in publishing_houses]), 200


@publishing_house.route('/<int:publishing_house_id>')
def get_by_id(publishing_house_id: int) -> jsonify:

    publishing_house = db.session.execute(db.select(PublishingHouse).filter_by(id=publishing_house_id)).scalar()

    return jsonify(publishing_house.to_dict()), 200


@publishing_house.route('/', methods=['POST'])
def create() -> jsonify:

    data = request.json
    publishing_house = PublishingHouse(name=data.get('name'), description=data.get('description'))

    db.session.add(publishing_house)
    db.session.commit()

    return jsonify(publishing_house.to_dict()), 201


@publishing_house.route('/<int:publishing_house_id>', methods=['PUT'])
def update(publishing_house_id: int) -> jsonify:

    publishing_house = db.session.execute(db.select(PublishingHouse).filter_by(id=publishing_house_id)).scalar()

    data = request.json
    publishing_house.name = data.get('name', publishing_house.name)
    publishing_house.description = data.get('description', publishing_house.description)

    db.session.commit()

    return jsonify(publishing_house.to_dict()), 201


@publishing_house.route('/<int:publishing_house_id>', methods=['DELETE'])
def delete(publishing_house_id: int) -> jsonify:

    publishing_house = db.session.execute(db.select(PublishingHouse).filter_by(id=publishing_house_id)).scalar()

    db.session.delete(publishing_house)
    db.session.commit()

    return jsonify(publishing_house.to_dict()), 204
