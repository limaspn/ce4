from fastapi import FastAPI
from app.services import gerar_previsoes

app = FastAPI(title="CE4 API")

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/previsao")
def previsao():
    return gerar_previsoes()