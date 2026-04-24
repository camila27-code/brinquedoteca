from pydantic import BaseModel
from datetime import date
from enum import Enum


class EmprestimoCreate(BaseModel):
    crianca_id: int
    brinquedo_id: int
    data_inicio: date
    data_fim: date

class EmprestimoOut(BaseModel):
    id: int
    crianca_id: int
    brinquedo_id: int
    data_inicio: date
    data_fim: date
    data_entrega: date | None
    status: str
    multa: float
