from fastapi import APIRouter

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo usuário.")
async def rota_criar_usuario(usuario):
    return{
        "mensagem": "Usuário cadastrado com sucesso."
    }