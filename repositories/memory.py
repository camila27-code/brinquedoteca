class MemoryDB:
    def __init__(self):
        self.criancas = {}
        self.brinquedos = {}
        self.emprestimos = {}
        self.next_criancas_id = 1
        self.next_brinquedos_id = 1
        self.next_emprestimos_id = 1

db = MemoryDB()
