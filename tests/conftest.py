from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from src.db import get_db
from app import create_app
from sqlalchemy import MetaData
import test_config
import contextlib

import pytest

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test

    alembic_config = AlembicConfig('alembic.ini')
    alembic_config.set_main_option('sqlalchemy.url', test_config.SQL_ALCHEMY_URL)
    alembic_upgrade(alembic_config, 'head')

    # create the app with common test config
    app = create_app({
      "DB_HOST": "127.0.0.1",
      "DB_PORT": "3307",
      "DB_USER": "root",
      "DB_PASS": "example",
      "DB_NAME": "test_task_db",
      "TESTING": True,
    })

    # create the database and load test data
    with app.app_context():
      test_db = get_db()

    yield app

    with app.app_context():
      db = get_db()
      db.execute("DELETE FROM task")
      db.dispose()
    # with contextlib.closing(test_db.connect()) as con:
    #   con.execute("TRUNCATE TABLE task")


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()