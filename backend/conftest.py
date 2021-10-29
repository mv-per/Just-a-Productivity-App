import os
import tempfile

import pytest
from . import create_app, db
from config import TestingConfig

# we create a pytest fixture called client() that configures the application for testing and initializes a new database
@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(True)

    temp_db_file = TestingConfig().DB_PATH
    print(temp_db_file)

    with app.test_client() as client:
        # with app.app_context():
        db.create_all()
        yield client

    # db.close()
    os.close(db_fd)
    os.unlink(db_path)
    os.remove(temp_db_file)
