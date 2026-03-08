from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from main import bcrypt_context
from dependencies import pegar_sessao

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get("/")
async def home():
    return {"mensagem": "Autentciação"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
       raise HTTPException(status_code=400, detail='E-mail do usuário já cadastrado')
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {'mensagem': f'Usuário cadastro com sucesso {email}'}
