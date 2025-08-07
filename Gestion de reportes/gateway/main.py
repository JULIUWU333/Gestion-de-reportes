from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Modulos.reportes.logica.reporte_service import router as reportes_router

app = FastAPI(title="API de Reportes Ciudadanos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aquí se incluyen los módulos (routers)
app.include_router(reportes_router, prefix="/reportes")
