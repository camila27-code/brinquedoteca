
from dataclasses import dataclass
from datetime import date
from enum import Enum

class EmprestimoStatus(Enum):
    ATIVO = "ativo"
    DEVOLVIDO = "devolvido"

@dataclass
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    data_inicio: date
    data_fim: date
    data_entrega: date | None = None
    status: EmprestimoStatus = EmprestimoStatus.ATIVO
    multa: float = 0.0
