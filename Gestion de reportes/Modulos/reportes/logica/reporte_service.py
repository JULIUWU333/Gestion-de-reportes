import json
from fastapi import APIRouter, Request, HTTPException
from Modulos.reportes.acceso_datos.get_factory import obtener_fabrica
from Modulos.reportes.acceso_datos.reporte_dto import ReporteDTO

dao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/")
async def crear_reporte(req: Request):
    data = await req.json()
    reporte = ReporteDTO(
        tip_id=data["tip_id"],
        rep_descripcion=data["rep_descripcion"],
        rep_url_imagen=data["rep_url_imagen"],
        rep_nivel_incidencia=int(data["rep_nivel_incidencia"]),
        usu_id=int(data["usu_id"])
    )
    dao.guardar(reporte)
    return {"mensaje": "Reporte almacenado correctamente."}

@router.get("/")
def obtener_reportes():
    return [r.__dict__ for r in dao.obtener_todos()]

@router.get("/{id}")
def obtener_reporte(id: int):
    reporte = dao.obtener_por_id(id)
    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return reporte.__dict__

@router.put("/{id}")
async def actualizar_reporte(id: int, req: Request):
    data = await req.json()
    actualizado = ReporteDTO(
   id=id,
    tip_id=int(data["tip_id"]),
    rep_descripcion=data["rep_descripcion"],
    rep_url_imagen=data["rep_url_imagen"],
    rep_nivel_incidencia=int(data["rep_nivel_incidencia"]),
    usu_id=int(data["usu_id"])
)
    dao.actualizar(actualizado)
    return {"mensaje": "Reporte actualizado"}

@router.delete("/{id}")
def eliminar_reporte(id: int):
    dao.eliminar(id)
    return {"mensaje": "Reporte eliminado"}
