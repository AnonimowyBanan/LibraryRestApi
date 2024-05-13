import pytest

from app import create_app
from app.config import TestingConfig
from app.extensions import db


@pytest.fixture(scope='session')
def app():
    app = create_app(TestingConfig)

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
