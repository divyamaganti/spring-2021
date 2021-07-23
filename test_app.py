import pytest
from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_hello_world(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data


def test_intro(client):
    response = client.get('/i')
    assert b'Divya Maganti is currently learning python to obtain a decent programming career after she graduate' \
           b' college.' in response.data


def test_body(client):
    response = client.get('/b')
    assert b'Divya Maganti is currently in high school and is aiming to attend either Rutgers University - New' \
           b'Brunswick, NYU, Stevens Institute of Technology or NJIT.' in response.data


def test_reverse(client):
    response = client.get('/reverse?word=buffalo')
    assert b'laffub' in response.data

