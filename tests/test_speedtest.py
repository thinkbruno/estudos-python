from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_speedtest_mocked():
    with patch("app.routers.speedtest_router.run_speedtest") as mock_speed:
        mock_speed.return_value = {"download_mbps": 100, "upload_mbps": 50}

        response = client.get("/speedtest")

        assert response.status_code == 200
        assert response.json()["download_mbps"] == 100
        assert response.json()["upload_mbps"] == 50
