from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_pdf():
    response = client.get("/generate-pdf")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert "attachment" in response.headers["content-disposition"]
