from Modulos.reportes.acceso_datos.conexion import ConexionDB
from Modulos.reportes.acceso_datos.mysql_Factory import MySQLReporteDAOFactory

def obtener_fabrica():
    conexion = ConexionDB()
    if conexion.motor == "mysql":
        return MySQLReporteDAOFactory()
    else:
        raise ValueError("Motor no soportado para reportes")
