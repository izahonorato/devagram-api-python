from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from routes.UserRoute import router as UsuarioRouter

app = FastAPI()

app.include_router(UsuarioRouter, tags=["Usuario"], prefix="/api/usuario")

@app.get("/api/health", tags=["Health"])
async def health():
    return{
        "status": "OK!"
    }