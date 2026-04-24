from typing import Dict, List, Optional
from datetime import date
from domain import Crianca, Brinquedo, Emprestimo

class CriancasRepo:
    def __init__(self):
        self._data: Dict[int, Crianca] = {}
        self._auto_id = 1

    def add(self, crianca: Crianca) -> Crianca:
        crianca.id = self._auto_id
        self._auto_id += 1
        self._data[crianca.id] = crianca
        return crianca

    def get(self, id: int) -> Crianca | None:
        return self._data.get(id)

    def list(self) -> List[Crianca]:
        return list(self._data.values())


class BrinquedosRepo:
    def __init__(self):
        self._data: Dict[int, Brinquedo] = {}
        self._auto_id = 1

    def add(self, brinquedo: Brinquedo) -> Brinquedo:
        brinquedo.id = self._auto_id
        self._auto_id += 1
        self._data[brinquedo.id] = brinquedo
        return brinquedo

    def get(self, id: int) -> Brinquedo | None:
        return self._data.get(id)

    def list(self) -> List[Brinquedo]:
        return list(self._data.values())

class EmprestimosRepo:
    def __init__(self):
        self._data: Dict[int, Emprestimo] = {}
        self._auto_id = 1

    def add(self, emprestimo: Emprestimo) -> Emprestimo:
        emprestimo.id = self._auto_id
        self._auto_id += 1
        self._data[emprestimo.id] = emprestimo
        return emprestimo

    def get(self, id: int) -> Emprestimo | None:
        return self._data.get(id)

    def list(self) -> List[Emprestimo]:
        return list(self._data.values())

    def list_by_crianca(self, crianca_id: int) -> List[Emprestimo]:
        return [e for e in self._data.values() if e.crianca_id == crianca_id]
