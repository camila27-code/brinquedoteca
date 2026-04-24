
from fastapi import APIRouter, HTTPException
from schemas import CriancaCreate, CriancaOut

router = APIRouter(prefix="/criancas", tags=["Crianças"])

@router.post("/", response_model=CriancaOut)
def criar_crianca(payload: CriancaCreate):
    crianca = service.criar_crianca(payload.nome, payload.idade, payload.responsavel)
    return crianca

@router.get("/", response_model=list[CriancaOut])
def listar_criancas():
    return service.criancas.list()

