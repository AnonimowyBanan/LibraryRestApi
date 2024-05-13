from app.extensions import db


class BookAuthor(db.Model):
    __tablename__ = 'book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, book_id: int, author_id: int):
        self.book_id = book_id
        self.author_id = author_id

    def __repr__(self):
        return f'<BookAuthor {self.id}>'
