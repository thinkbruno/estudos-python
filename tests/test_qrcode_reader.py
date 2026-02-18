from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_qrcode_no_file():
    response = client.post("/read-qrcode")
    assert response.status_code == 422
