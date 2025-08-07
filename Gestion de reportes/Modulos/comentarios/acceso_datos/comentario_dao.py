
from modulos.comentarios.acceso_datos.comentario_dto import ComentarioDTO
from modulos.comentarios.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class ComentarioDAOMySQL:
    def guardar(self, comentario_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO comentarios (texto, usuario_email, calificacion, fecha) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (comentario_dto.texto, comentario_dto.usuario_email, comentario_dto.calificacion, comentario_dto.fecha))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, texto, usuario_email, calificacion, fecha FROM comentarios")
            rows = cursor.fetchall()
        return [ComentarioDTO(id=row[0], texto=row[1], usuario_email=row[2], calificacion=row[3], fecha=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, texto, usuario_email, calificacion, fecha FROM comentarios WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ComentarioDTO(id=row[0], texto=row[1], usuario_email=row[2], calificacion=row[3], fecha=row[4])
        return None

    def actualizar(self, comentario_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE comentarios SET texto = %s, usuario_email = %s, calificacion = %s WHERE id = %s"
            cursor.execute(sql, (comentario_dto.texto, comentario_dto.usuario_email, comentario_dto.calificacion, comentario_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM comentarios WHERE id = %s", (id,))
        conn.commit()

class ComentarioDAOPostgres:
    def guardar(self, comentario_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO comentarios (texto, usuario_email, calificacion, fecha) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (comentario_dto.texto, comentario_dto.usuario_email, comentario_dto.calificacion, comentario_dto.fecha))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, texto, usuario_email, calificacion, fecha FROM comentarios")
            rows = cursor.fetchall()
        return [ComentarioDTO(id=row[0], texto=row[1], usuario_email=row[2], calificacion=row[3], fecha=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, texto, usuario_email, calificacion, fecha FROM comentarios WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ComentarioDTO(id=row[0], texto=row[1], usuario_email=row[2], calificacion=row[3], fecha=row[4])
        return None

    def actualizar(self, comentario_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE comentarios SET texto = %s, usuario_email = %s, calificacion = %s WHERE id = %s"
            cursor.execute(sql, (comentario_dto.texto, comentario_dto.usuario_email, comentario_dto.calificacion, comentario_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM comentarios WHERE id = %s", (id,))
        conn.commit()
