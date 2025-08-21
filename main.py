from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/suicidio")
async def teste():
    return {"vou me matar domingo"}