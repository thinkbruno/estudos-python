from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_number():
    response = client.get("/discover-operator?number=13999999999")

    assert response.status_code == 200
    assert "operadora" in response.json()
    assert "estado" in response.json()


def test_invalid_number():
    response = client.get("/discover-operator?number=abc")

    assert response.status_code == 400
