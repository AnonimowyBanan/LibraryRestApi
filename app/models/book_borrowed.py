from app.extensions import db
from sqlalchemy_serializer import SerializerMixin


class BookBorrowed(db.Model, SerializerMixin):
    __tablename__ = 'books_borrowed'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    borrowed_at = db.Column(db.DateTime, server_default=db.func.now())
    returned_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    book = db.relationship('Book', backref=db.backref('book_borrowed', uselist=False))
    user = db.relationship('User', backref=db.backref('book_borrowed', uselist=False))

    def __init__(self, book_id: int, user_id: int) -> None:
        self.book_id = book_id
        self.user_id = user_id

    def __repr__(self) -> str:
        return f'<BookBorrowed {self.id}>'
