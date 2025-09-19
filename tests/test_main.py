from fastapi.testclient import TestClient
from main import app, minha_funcao

client = TestClient(app)

# 1. Teste unitário da função principal
def test_minha_funcao():
    assert minha_funcao() is True

# 2. Teste do endpoint raiz
def test_root_endpoint_status():
    response = client.get("/")
    assert response.status_code == 200

# 3. Teste do conteúdo do endpoint raiz
def test_root_endpoint_content():
    response = client.get("/")
    data = response.json()
    assert "teste" in data

# 4. Teste do endpoint /deps
def test_deps_endpoint_status():
    response = client.get("/deps")
    assert response.status_code == 200

# 5. Teste do conteúdo do endpoint /deps
def test_deps_endpoint_content():
    response = client.get("/deps")
    data = response.json()
    assert "tenho ansiedade" in data
