
from datetime import datetime

class ComentarioDTO:
    def __init__(self, id=None, texto="", usuario_email="", calificacion=0, fecha=None):
        self.id = id
        self.texto = texto
        self.usuario_email = usuario_email
        self.calificacion = calificacion
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"ComentarioDTO(id={{self.id}}, texto='{{self.texto}}', usuario_email='{{self.usuario_email}}', calificacion={{self.calificacion}}, fecha={{self.fecha}})"
