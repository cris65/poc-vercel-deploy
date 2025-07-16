# Contenuto per: api/index.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Questa è l'intera applicazione
app = FastAPI()

# Aggiungiamo il CORS per permettere alla pagina HTML di chiamare l'API in locale
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Per questo test, permettiamo qualsiasi origine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def get_hello_message():
    """Un semplice endpoint di test."""
    return {"message": "✅ Backend is alive and responding!"}