
import pytest
from app import app
import database


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        database.create_table()
        yield test_client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_students(client):
    response = client.get(
        "/api/students",
        headers={"X-API-Key": "student123456"}
    )
    assert response.status_code == 200


def test_add_student(client):
    response = client.post(
        "/api/students",
        json={
            "name": "Test Student",
            "course": "BCA",
            "email": "teststudent@example.com"
        },
        headers={"X-API-Key": "student123456"}
    )
    assert response.status_code == 201


def test_missing_api_key(client):
    response = client.get("/api/students")
    assert response.status_code == 401
