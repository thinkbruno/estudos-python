from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_json_generator_status_code():
    response = client.get("/json-generator")
    assert response.status_code == 200


def test_json_generator_headers():
    response = client.get("/json-generator")

    assert response.headers["content-type"] == "application/json"
    assert "attachment" in response.headers["content-disposition"]
    assert "data.json" in response.headers["content-disposition"]


def test_json_generator_content_is_valid_json():
    response = client.get("/json-generator")

    data = json.loads(response.content)

    assert "nome" in data
    assert "usuario" in data
    assert "senha" in data
    assert "dados_pessoais" in data
