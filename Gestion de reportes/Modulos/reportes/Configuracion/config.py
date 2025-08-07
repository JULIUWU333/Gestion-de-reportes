# configuracion/config.py

import json

def cargar_configuracion(path="Modulos/reportes/Configuracion/config.json"):
    with open(path) as f:
        return json.load(f)

