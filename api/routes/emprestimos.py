from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from domain.emprestimos import EmprestimoStatus
from schemas import EmprestimoCreate, EmprestimoOut

router = APIRouter(prefix="/emprestimos", tags=["Empréstimos"])


@router.post("/", response_model=EmprestimoOut)
def criar_emprestimo(payload: EmprestimoCreate):
    try:
        emprestimo = service.criar_emprestimo(payload.crianca_id, payload.brinquedo_id, payload.data_inicio, payload.data_fim)
        return emprestimo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[EmprestimoOut])
def listar_emprestimos():
    return service.emprestimos.list()

@router.get("/{id}", response_model=EmprestimoOut)
def obter_emprestimo(id: int):
    e = service.emprestimos.get(id)
    if not e:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return e

@router.put("/{id}/devolver", response_model=EmprestimoOut)
def devolver_emprestimo(id: int):
    try:
        e = service.devolver_emprestimo(id)
        return e
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
