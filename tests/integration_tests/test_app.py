import pytest
from app import app
from flaskr.util.createdb import create_db
from unittest.mock import patch
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
    flask_app.config['WTF_CSRF_ENABLED'] = False
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_create_user(test_client):
    # Given
    request_payload = {
        "username": "foulen",
        "email": "foulen@gmail.com",
        "password": "12345678"
    }

    expected_page_content=b"You have created an account foulen"
    expected_status_code = 200


    #When
    response = test_client.post('/signup', data=request_payload, follow_redirects=True)

    # Then
    assert expected_status_code == response.status_code
    assert expected_page_content in response.data

def test_login(test_client):
    # Given
    request_payload = {
        "username": "foulen",
        "password": "12345678"
    }

    expected_page_content=b"You have connected foulen"
    expected_status_code = 200


    #When
    response = test_client.post('/login', data=request_payload, follow_redirects=True)

    # Then
    assert expected_status_code == response.status_code
    assert expected_page_content in response.data



