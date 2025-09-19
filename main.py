from fastapi import FastAPI

app = FastAPI()


def minha_funcao():
    return True


@app.get("/")
async def root():
 return {"teste"}


@app.get("/deps")
async def teste():

    return {"mensagem": "tenho ansiedade"}

