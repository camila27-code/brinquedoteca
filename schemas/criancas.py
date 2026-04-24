from pydantic import BaseModel


class CriancasCreate(BaseModel):
     id: int
     nome: str
     idade: int
     responsavel: str
    

class CriancasOut(BaseModel):
    id: int
    nome: str
    idade: int
    responsavel: str
