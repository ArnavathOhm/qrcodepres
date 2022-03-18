from app import app
from db_connect import Database
import cypter
import pytest


app.config.update(TESTING=True, DATABASE="test.db")
connect = Database("test.db")
connect.create()


@pytest.fixture(scope="module")
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
            connect.delete_all()
            connect.db.commit()


def test_index_no_id(test_client):
    response = test_client.get("/")
    assert response.status_code == 400


def test_index_id_no_exists(test_client):
    id = connect.generate_id()
    id_key = cypter.encriptIT(id).decode("utf-8")
    response = test_client.get("/?id=" + id_key)
    assert response.status_code == 400


def test_index_error_decrypt_id(test_client):
    id_key = "abcdefghijklmnopqrstuvwqyz1234567"
    response = test_client.get("/?id=" + id_key)
    assert response.status_code == 400


def test_index_success(test_client):
    id = connect.generate_id()
    connect.add_user(id, "test")
    connect.db.commit()

    id_key = cypter.encriptIT(id).decode("utf-8")
    response = test_client.get("/?id=" + id_key)
    assert response.status_code == 200
