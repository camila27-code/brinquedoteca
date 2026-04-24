from dataclasses import dataclass

@dataclass
class Brinquedos:
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True

    
