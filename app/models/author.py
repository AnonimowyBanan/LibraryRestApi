from app.extensions import db
from sqlalchemy_serializer import SerializerMixin


class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    biography = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, first_name: str, last_name: str, biography: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography

    def __repr__(self) -> str:
        return f'<Author {self.name}>'
