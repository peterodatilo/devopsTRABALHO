from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_status():
    response = client.get("/")
    assert response.status_code == 200

def test_root_content():
    response = client.get("/")
    assert response.json() == {"msg": "teste"}

def test_deps_status():
    response = client.get("/deps")
    assert response.status_code == 200

def test_deps_content():
    response = client.get("/deps")
    assert "ansiosidade" in response.json()["msg"]

def test_invalid_route():
    response = client.get("/rota_inexistente")
    assert response.status_code == 404
