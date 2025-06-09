import pytest
from flask.testing import FlaskClient
from app import app
from typing import Generator

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    """Fixture to create a test client for the Flask app.

    Yields:
        FlaskClient: Test client for the Flask application.
    """
    with app.test_client() as client:
        yield client

def test_hello_world(client: FlaskClient) -> None:
    """Test the root endpoint '/'.

    Args:
        client (FlaskClient): The Flask test client.

    Asserts:
        The response status code is 200 and response data is 'Hello World'.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello World"

def test_health_ok(client: FlaskClient) -> None:
    """Test the '/health' endpoint for healthy status.

    Args:
        client (FlaskClient): The Flask test client.

    Asserts:
        The response status code is 200 and JSON status is 'ok'.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok"}