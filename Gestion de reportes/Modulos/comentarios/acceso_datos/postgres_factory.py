from modulos.comentarios.acceso_datos.comentario_dao import ComentarioDAOPostgres
from modulos.comentarios.acceso_datos.dao_factory import ComentarioDAOFactory

class PostgresComentarioDAOFactory(ComentarioDAOFactory):
    def crear_dao(self):
        return ComentarioDAOPostgres()