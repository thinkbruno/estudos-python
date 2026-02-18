from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_qrcode():
    response = client.get("/generate-qrcode?url=https://google.com")

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_generate_qrcode_invalid_url():
    response = client.get("/generate-qrcode?url=invalid-url")

    assert response.status_code == 400
    assert response.json() == {"detail": "URL inválida"}
