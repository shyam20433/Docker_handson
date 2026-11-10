
import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homePage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {
        "Message": "This is Home Page"
    }


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {
        "status": "Up"
    }


def test_invalid_route(client):
    response = client.get("/invalid")

    assert response.status_code == 404


def test_home_content_type(client):
    response = client.get("/")

    assert response.content_type == "application/json"
