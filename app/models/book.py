from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

from app.extensions import db


class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    publishing_house_id = db.Column(db.Integer, db.ForeignKey('publishing_houses.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    authors = relationship('BookAuthor', backref='book', cascade="all,delete")

    def __init__(self, title: str, author: str, year: int, publishing_house_id: int):
        self.title = title
        self.author = author
        self.year = year
        self.publishing_house_id = publishing_house_id

    def __repr__(self):
        return f'<Book {self.title}>'
