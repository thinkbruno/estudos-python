from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_invalid_url():
    response = client.get("/download-text?url=invalid-url")

    assert response.status_code == 400
