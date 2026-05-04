from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services import gerar_previsoes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/previsao")
def previsao():
    return {
        "data": gerar_previsoes()
    }