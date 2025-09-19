import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from main import app, minha_funcao
from fastapi.testclient import TestClient

client = TestClient(app)


def test_minha_funcao():
    """Verifica se a função principal retorna True"""
    assert minha_funcao() is True


def test_root():
    """Verifica se o endpoint raiz responde corretamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert "teste" in response.json()


def test_deps():
    """Verifica se o endpoint /deps responde corretamente"""
    response = client.get("/deps")
    assert response.status_code == 200
    assert "mensagem" in response.json()
