from flask import request, jsonify

from . import book
from app.models import Book, BookAuthor
from app.extensions import db


@book.route('/')
def get() -> jsonify:

    books = db.session.execute(db.select(Book)).scalars()

    return jsonify([book.to_dict() for book in books]), 200


@book.route('/<int:book_id>')
def get_by_id(book_id: int) -> jsonify:

    book = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar()

    return jsonify(book.to_dict()), 200


@book.route('/', methods=['POST'])
def create() -> jsonify:

    data = request.json

    try:
        with db.session() as session:
            session.begin_nested()
            book = Book(title=data.get('title'), author=data.get('author'), year=data.get('year'),
                        publishing_house_id=data.get('publishing_house_id'))
            session.add(book)
            session.flush()

            for author_id in data.get('authors_ids'):
                author = BookAuthor(book_id=book.id, author_id=author_id)
                session.add(author)

            session.commit()
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400

    return jsonify(book.to_dict()), 201


@book.route('/<int:book_id>', methods=['PUT'])
def update(book_id: int) -> jsonify:

    data = request.json

    try:
        with db.session() as session:
            session.begin_nested()
            book = session.execute(db.select(Book).filter_by(id=book_id)).scalar()

            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.year = data.get('year', book.year)
            book.publishing_house_id = data.get('publishing_house_id', book.publishing_house_id)

            if data.get('authors_ids'):
                authors = session.execute(db.delete(BookAuthor).filter_by(book_id=book_id)).scalars()
                db.session.delete(authors)
                for author_id in data.get('authors_ids'):
                    author = BookAuthor(book_id=book_id, author_id=author_id)
                    session.add(author)
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400

    return jsonify(book.to_dict()), 200


@book.route('/<int:book_id>', methods=['DELETE'])
def delete(book_id: int) -> jsonify:

        try:
            with db.session() as session:
                book = session.execute(db.select(Book).filter_by(id=book_id)).scalar()
                session.delete(book)
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 400

        return jsonify({'message': 'Book deleted successfully'}), 200