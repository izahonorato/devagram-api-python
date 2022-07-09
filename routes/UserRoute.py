from fastapi import APIRouter

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo usuário.")