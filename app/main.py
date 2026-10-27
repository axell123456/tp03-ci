from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "Bienvenue sur le TP03"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "1.0"}
