from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services import gerar_previsoes

app = FastAPI(title="CE4 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/previsao")
def previsao():
    return {
        "data": gerar_previsoes()
    }