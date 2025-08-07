import json
import pymysql

class ConexionDB:
    def __init__(self):
        with open("Modulos/reportes/configuracion/config.json") as f:
            config = json.load(f)

        self.motor = config.get("db_engine")

        if self.motor == "mysql":
            self.config = {
                "host": config["host"],
                "port": config["port"],
                "user": config["user"],
                "password": config["password"],
                "database": config["database"]
            }
        else:
            raise ValueError("Motor de base de datos no soportado")

    def obtener_conexion(self):
        return pymysql.connect(**self.config)
