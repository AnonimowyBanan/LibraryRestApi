from app.extensions import db
from sqlalchemy_serializer import SerializerMixin


class PublishingHouse(db.Model, SerializerMixin):
    __tablename__ = 'publishing_houses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f'<PublishingHouse {self.name}>'