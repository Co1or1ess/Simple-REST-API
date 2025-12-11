import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.json["message"] == "Hello world!"

def test_add(client):
    res = client.get("/add?x=3&y=4")
    assert res.status_code == 200
    assert res.json["result"] == 7

def test_add_default(client):
    res = client.get("/add")
    assert res.json["result"] == 0
