from pydantic import BaseModel


class BrinquedosCreat (BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True


class BrinquedosCreat (BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True
