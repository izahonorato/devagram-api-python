from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/health", tags=["Health"])
async def health():
    return{
        "status": "OK!"
    }