import pytest
from app import app
from flaskr.util.createdb import create_db
import os


@pytest.fixture(scope="session",autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_access_unpriveleged_page(test_client):
    # Given
    request_payload = {
        "username": "foulen",
        "email": "foulen@gmail.com",
        "password": "12345678"
    }

    expected_status_code = 200
    expected_path = "/login"


    # When
    response = test_client.get('/dashboard', follow_redirects=True)

    # Then
    print(response.request.path)
    print(response.history)
    print(response.status_code)

    assert expected_status_code == response.status_code
    assert expected_path == response.request.path






