from fastapi import APIRouter, HTTPException, status

from schemas.emprestimos import EmprestimosCreate, EmprestimosOut
from services.emprestimos_services import(
    ErrosValidacoes,
    buscar_id,
    crianca_id,
    brinquedo_id,
    datas,
    status,
    multas,
)

router = APIRouter(prefix="/buscar_id", tags=["buscar_id"])


@router.post("", response_model=EmprestimosOut, status_code=status.HTTP_201_CREATED)
def buscar_id_route(data: EmprestimosCreate):
    try:
        return buscar_id(**data.model_dump())
    except ErrosValidacoes as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.mensagens)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)) 


@router.get("", response_model=list[EmprestimosOut])
def listar_emprestimos_routs():
    return listar_emprestimos_routs()



@router.get("/emprestimos/{crianca_id, brinquedo_id}", response_model=list[EmprestimosOut])
def listar_emprestimos_route(emprestimos_id: int):
    try:
        return emprestimos_id(emprestimos_id)
    except ErrosValidacoes as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, e.mensagens)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))



@router.put("eprestimos/{crianca_id,}/devolver")
def cancelar_emprestimos_route(emprestimos_id: int):
    try:
        return devolver_emprestimos(emprestimos_id)
    except ErrosValidacoes as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.mensagens)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))



@router.put("/{brinquedos_id,}/emprestimos")
def finalizar_reserva_route(reserva_id: int, hora_atual: str):
    try:
        return listar_emprestimos_route(crianca_id, brinquedo_id)
    except ErrosValidacoes as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.mensagens)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
    
