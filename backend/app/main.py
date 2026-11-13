import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.dashboard_API_controller import DashboardAPIController

app = FastAPI(
    title="API TCC - Violência Contra Mulheres",
    version="1.0.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instancia o controller que mapeia as rotas orientado a objetos
dashboard_controller = DashboardAPIController()

# Inclui as rotas na aplicação principal
app.include_router(dashboard_controller.router)