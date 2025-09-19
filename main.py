"""
Módulo principal da aplicação FastAPI.
"""

from fastapi import FastAPI

app = FastAPI()


def minha_funcao():
    """
    Função de exemplo que retorna True.
    """
    return True


@app.get("/")
async def root():
    """
    Endpoint raiz da aplicação.
    """
    return {"teste"}


@app.get("/deps")
async def teste():
    """
    Endpoint de exemplo que retorna uma mensagem fixa.
    """
    return {"mensagem": "tenho ansiedade"}

