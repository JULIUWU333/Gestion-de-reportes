from Modulos.reportes.acceso_datos.reporte_dto import ReporteDTO
from Modulos.reportes.acceso_datos.conexion import ConexionDB


class ReporteDAOMySQL:

    def guardar(self, reporte: ReporteDTO):
        conn = ConexionDB().obtener_conexion()
        cursor = conn.cursor()
        sql = """
            INSERT INTO reporte (tip_id, rep_descripcion, rep_url_imagen, rep_nivel_incidencia, usu_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (reporte.tip_id, reporte.rep_descripcion, reporte.rep_url_imagen, reporte.rep_nivel_incidencia, reporte.usu_id))
        conn.commit()
        conn.close()

    def obtener_todos(self):
        conn = ConexionDB().obtener_conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM reporte"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conn.close()
        return [ReporteDTO(id=row[0], tip_id=row[1], rep_descripcion=row[2], rep_url_imagen=row[3], rep_nivel_incidencia=row[4], usu_id=row[5]) for row in resultados]

    def obtener_por_id(self, id: int):
        conn = ConexionDB().obtener_conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM reporte WHERE rep_id = %s"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return ReporteDTO(id=row[0], tip_id=row[1], rep_descripcion=row[2], rep_url_imagen=row[3], rep_nivel_incidencia=row[4], usu_id=row[5])
        return None

    def actualizar(self, reporte: ReporteDTO):
        conn = ConexionDB().obtener_conexion()
        cursor = conn.cursor()
        sql = """
            UPDATE reporte
            SET tip_id = %s, rep_descripcion = %s, rep_url_imagen = %s,
                rep_nivel_incidencia = %s, usu_id = %s
            WHERE rep_id = %s
        """
        cursor.execute(sql, (
            reporte.tip_id, reporte.rep_descripcion, reporte.rep_url_imagen,
            reporte.rep_nivel_incidencia, reporte.usu_id, reporte.id
        ))
        conn.commit()
        conn.close()

    def eliminar(self, id: int):
        conn = ConexionDB().obtener_conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM reporte WHERE rep_id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
        conn.close()
