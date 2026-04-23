from fastapi import FastAPI
from api.routes.criancas import router as criancas_router
from api.routes.brinquedos import router as brinquedos_router
from api.routes.emprestimos import router as emprestimos_router

app = FastAPI(
                title="", 
                description="API para controlar empréstimos de brinquedos para crianças", 
                version="1.0.0"
            )

app.include_router(criancas_router)
app.include_router(brinquedos_router)
app.include_router(emprestimos_router)
