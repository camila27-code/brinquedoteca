from pydantic import BaseModel


class EmprestimosCreate(BaseModel):
     id: int
     crianca_id: int
     brinquedo_id: int
     datas: str
     status: str
     multa: int
    

class EmprestimosOut(BaseModel):
     id: int
     crianca_id: int
     brinquedo_id: int
     datas: str
     status: str
     multa: int
