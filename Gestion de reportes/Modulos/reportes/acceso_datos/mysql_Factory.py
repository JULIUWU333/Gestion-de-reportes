from Modulos.reportes.acceso_datos.reporte_dao import ReporteDAOMySQL
from Modulos.reportes.acceso_datos.dao_factory import ReporteDAOFactory

class MySQLReporteDAOFactory(ReporteDAOFactory):
    def crear_dao(self):
        return ReporteDAOMySQL()
