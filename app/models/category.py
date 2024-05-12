from app.extensions import db
from sqlalchemy_serializer import SerializerMixin


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Category {self.name}>'
