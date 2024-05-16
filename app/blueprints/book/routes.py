from flask import request, jsonify

from . import book
from app.models import Book, BookAuthor
from app.extensions import db


@book.route('/', methods=['POST'])
def create() -> jsonify:
    data = request.json

    session = db.session()

    try:
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
    finally:
        session.close()

    return jsonify(book.to_dict()), 201
