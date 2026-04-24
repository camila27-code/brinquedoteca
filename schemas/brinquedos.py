from pydantic import BaseModel
from datetime import date
from enum import Enum


class BrinquedoCreate(BaseModel):
    nome: str
    categoria: str
    faixa_etaria_minima: int

class BrinquedoOut(BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool
