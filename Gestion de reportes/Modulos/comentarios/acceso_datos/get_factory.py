from modulos.comentarios.configuracion.config import cargar_configuracion
from modulos.comentarios.acceso_datos.mysql_factory import MySQLComentarioDAOFactory
from modulos.comentarios.acceso_datos.postgres_factory import PostgresComentarioDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresComentarioDAOFactory()
    return MySQLComentarioDAOFactory()