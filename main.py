"""
Módulo principal da aplicação.
"""

def minha_funcao():
    """Executa a lógica principal."""
    return True


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"teste"}

@app.get("/deps")
async def teste():
    return {"tenho ansiedade"}