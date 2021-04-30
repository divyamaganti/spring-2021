import pytest
from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_hello_world(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data
