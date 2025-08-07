from modulos.comentarios.acceso_datos.comentario_dao import ComentarioDAOMySQL
from modulos.comentarios.acceso_datos.dao_factory import ComentarioDAOFactory

class MySQLComentarioDAOFactory(ComentarioDAOFactory):
    def crear_dao(self):
        return ComentarioDAOMySQL()