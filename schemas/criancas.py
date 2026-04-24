from pydantic import BaseModel
from datetime import date
from enum import Enum

class CriancaCreate(BaseModel):
    nome: str
    idade: int
    responsavel: str

class CriancaOut(BaseModel):
    id: int
    nome: str
    idade: int
    responsavel: str
    bloqueado: bool
    atrasos: int
