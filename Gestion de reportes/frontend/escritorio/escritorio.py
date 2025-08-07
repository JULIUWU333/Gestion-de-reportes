import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("Modulos/reportes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

# Ventana principal
root = tk.Tk()
root.title("Gestión de Reportes")

# Tabla
cols = ("ID", "Tipo", "Descripción", "URL Imagen", "Incidencia", "Usuario")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=140)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Recargar datos en tabla
def recargar_datos():
    for item in tree.get_children():
        tree.delete(item)
    try:
        r = requests.get(API + ENDPOINTS["read_all"])
        if r.status_code == 200:
            for rep in r.json():
                tree.insert("", "end", values=(
                    rep["id"], rep["tip_id"], rep["rep_descripcion"],
                    rep["rep_url_imagen"], rep["rep_nivel_incidencia"], rep["usu_id"]
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear nuevo reporte
def crear_reporte():
    dialogo_reporte("Crear nuevo reporte")

# Editar reporte seleccionado
def editar_reporte():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un reporte.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_reporte("Editar reporte", valores)

# Eliminar reporte seleccionado
def eliminar_reporte():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un reporte.")
        return
    rep_id = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Está seguro que desea eliminar este reporte?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(rep_id)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "Reporte eliminado.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Diálogo de reporte (crear o editar)
def dialogo_reporte(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)

    labels = ["Tipo ID:", "Descripción:", "URL Imagen:", "Incidencia (1-5):", "Usuario ID:"]
    entradas = []

    for i, label in enumerate(labels):
        tk.Label(ventana, text=label).grid(row=i, column=0)
        entry = tk.Entry(ventana)
        entry.grid(row=i, column=1)
        entradas.append(entry)

    if datos:
        rep_id, tip_id, desc, url, incidencia, usu_id = datos
        entradas[0].insert(0, tip_id)
        entradas[1].insert(0, desc)
        entradas[2].insert(0, url)
        entradas[3].insert(0, incidencia)
        entradas[4].insert(0, usu_id)

    def guardar():
        payload = {
            "tip_id": int(entradas[0].get()),
            "rep_descripcion": entradas[1].get(),
            "rep_url_imagen": entradas[2].get(),
            "rep_nivel_incidencia": int(entradas[3].get()),
            "usu_id": int(entradas[4].get())
        }
        try:
            if datos:
                r = requests.put(API + ENDPOINTS["update"].replace("{id}", str(rep_id)), json=payload)
            else:
                r = requests.post(API + ENDPOINTS["create"], json=payload)
            if r.status_code in [200, 201]:
                recargar_datos()
                ventana.destroy()
                messagebox.showinfo("Éxito", "Operación exitosa.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, columnspan=2, pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nuevo", command=crear_reporte).pack(side="left", padx=5)
tk.Button(botonera, text="Editar", command=editar_reporte).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar", command=eliminar_reporte).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar", command=recargar_datos).pack(side="left", padx=5)

recargar_datos()
root.mainloop()
