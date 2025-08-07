import requests
import json

# Cargar configuración desde config.json
with open("Modulos/reportes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú Reportes =====")
    print("1. Ingresar nuevo reporte")
    print("2. Listar reportes")
    print("3. Obtener reporte por ID")
    print("4. Actualizar reporte")
    print("5. Eliminar reporte")
    print("6. Salir")

def ingresar():
    tip_id = input("ID del tipo de reporte: ")
    descripcion = input("Descripción del reporte: ")
    url_imagen = input("URL de la imagen: ")
    nivel = input("Nivel de incidencia (1-5): ")
    usu_id = input("ID del usuario que reporta: ")

    r = requests.post(f"{API}{ENDPOINTS['create']}", json={
        "tip_id": int(tip_id),
        "rep_descripcion": descripcion,
        "rep_url_imagen": url_imagen,
        "rep_nivel_incidencia": int(nivel),
        "usu_id": int(usu_id)
    })

    print("STATUS:", r.status_code)
    print("RESPUESTA BRUTA:", r.text)

    try:
        print("RESPUESTA JSON:", r.json())
    except Exception:
        print("La respuesta no fue JSON válida.")

def listar():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    for rep in r.json():
        print(rep)

def obtener():
    id = input("ID del reporte: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    print(r.json() if r.status_code == 200 else "Reporte no encontrado.")

def actualizar():
    id = input("ID a actualizar: ")
    tip_id = input("Nuevo ID del tipo de reporte: ")
    descripcion = input("Nueva descripción: ")
    url_imagen = input("Nueva URL de la imagen: ")
    nivel = input("Nuevo nivel de incidencia: ")
    usu_id = input("Nuevo ID del usuario: ")
    url = ENDPOINTS["update"].replace("{id}", id)
    r = requests.put(f"{API}{url}", json={
        "tip_id": int(tip_id),
        "rep_descripcion": descripcion,
        "rep_url_imagen": url_imagen,
        "rep_nivel_incidencia": int(nivel),
        "usu_id": int(usu_id)
    })
    print(r.json())

def eliminar():
    id = input("ID a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1": ingresar()
        elif opcion == "2": listar()
        elif opcion == "3": obtener()
        elif opcion == "4": actualizar()
        elif opcion == "5": eliminar()
        elif opcion == "6": break
        else: print("Opción inválida.")
