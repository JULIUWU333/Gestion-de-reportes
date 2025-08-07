import json
from fastapi import APIRouter, Request, HTTPException
from modulos.comentarios.acceso_datos.get_factory import obtener_fabrica
from modulos.comentarios.acceso_datos.comentario_dto import ComentarioDTO
from modulos.comentarios.notificaciones.sujeto import ComentarioSubject
from modulos.comentarios.notificaciones.observador import UsuarioNotificador, AdminNotificador
dao = obtener_fabrica().crear_dao()
sujeto = ComentarioSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())
router = APIRouter()

@router.post("/")
async def crear_comentario(req: Request):
    data = await req.json()
    comentario = ComentarioDTO(
        texto=data["texto"],usuario_email=data["usuario_email"],calificacion=int(data["calificacion"]) )
    dao.guardar(comentario)
    if comentario.calificacion <= 2:
        sujeto.notificar(comentario)
    return {"mensaje": "Comentario almacenado correctamente."}
@router.get("/")
def obtener_comentarios():
    return [c.__dict__ for c in dao.obtener_todos()]
@router.get("/{id}")
def obtener_comentario(id: int):
    comentario = dao.obtener_por_id(id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comentario.__dict__
@router.put("/{id}")
async def actualizar_comentario(id: int, req: Request):
    data = await req.json()
    actualizado = ComentarioDTO(
        id=id,
        texto=data["texto"],
        usuario_email=data["usuario_email"],
        calificacion=int(data["calificacion"])
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Comentario actualizado"}
@router.delete("/{id}")
def eliminar_comentario(id: int):
    dao.eliminar(id)
    return {"mensaje": "Comentario eliminado"}
