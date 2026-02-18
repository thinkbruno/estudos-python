from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_pc_info():
    response = client.get("/pc-info")

    assert response.status_code == 200
    assert "architecture" in response.json()
