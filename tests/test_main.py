import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from main import app, minha_funcao
from fastapi.testclient import TestClient

client = TestClient(app)


def test_minha_funcao():

    assert minha_funcao() is True


def test_root():

    response = client.get("/")
    assert response.status_code == 200
    assert "teste" in response.json()


def test_deps():

    response = client.get("/deps")
    assert response.status_code == 200
    assert "mensagem" in response.json()
