import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/comentarios/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, comentario):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, comentario):
        mensaje = f"[Usuario] Se envió alerta al usuario {comentario.usuario_email} por su comentario negativo."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, comentario):
        mensaje = f"[Admin] Atención: Comentario negativo registrado de {comentario.usuario_email}: '{comentario.texto}'"
        print(mensaje)
        logging.info(mensaje)
