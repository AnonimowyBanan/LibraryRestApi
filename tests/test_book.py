import pytest

from .conftest import client
from app.models import Author, PublishingHouse
from app.extensions import db
from app import app

prefix = "/book/"

test_author_data1 = {"first_name": "Test Author Name", "last_name": "Test Author Last Name",
                     "biography": "Test Biography"}
test_author_data2 = {"first_name": "Test Author Name Second", "last_name": "Test Author Last Name Second",
                     "biography": "Test Biography Second"}
test_publishing_house_data = {"name": "Test Publishing House", "description": "Test Description"}


@pytest.fixture(scope='module')
def test_create(client, app):
    with app.app_context():
        author1 = Author(**test_author_data1)
        author2 = Author(**test_author_data2)
        publishing_house = PublishingHouse(**test_publishing_house_data)

        db.session.add_all([author1, author2, publishing_house])

        db.session.commit()

    data = {
        "title": "Test Book",
        "authors_ids": [author1.id, author2.id],
        "year": 2021,
        "publishing_house_id": publishing_house.id
    }

    response = client.post(prefix, json=data)

    assert response.status_code == 201
