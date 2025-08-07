async function listarReportes() {
    const res = await fetch(API_BASE + ENDPOINTS.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaReportes");
    lista.innerHTML = "";
    data.forEach(r => {
        const item = document.createElement("li");
        item.textContent = `ID: ${r.rep_id} - Tipo: ${r.tip_id} - ${r.rep_descripcion} (Nivel: ${r.rep_nivel_incidencia}) - Usuario: ${r.usu_id}`;
        lista.appendChild(item);
    });
}

document.getElementById("formReporte").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        tip_id: parseInt(document.getElementById("tip_id").value),
        rep_descripcion: document.getElementById("rep_descripcion").value,
        rep_url_imagen: document.getElementById("rep_url_imagen").value,
        rep_nivel_incidencia: parseInt(document.getElementById("rep_nivel_incidencia").value),
        usu_id: parseInt(document.getElementById("usu_id").value)
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Reporte creado.");
    listarReportes();
    mostrarSeccion('lista');
});

async function buscarReporte() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("tip_idAccion").value = data.tip_id;
        document.getElementById("rep_descripcionAccion").value = data.rep_descripcion;
        document.getElementById("rep_url_imagenAccion").value = data.rep_url_imagen;
        document.getElementById("rep_nivel_incidenciaAccion").value = data.rep_nivel_incidencia;
        document.getElementById("usu_idAccion").value = data.usu_id;
        mostrarSeccion('acciones');
        alert("Reporte cargado para edición.");
    } else {
        alert("Reporte no encontrado.");
    }
}

async function actualizarReporte() {
    const id = document.getElementById("idBuscar").value;
    const body = {
        tip_id: parseInt(document.getElementById("tip_idAccion").value),
        rep_descripcion: document.getElementById("rep_descripcionAccion").value,
        rep_url_imagen: document.getElementById("rep_url_imagenAccion").value,
        rep_nivel_incidencia: parseInt(document.getElementById("rep_nivel_incidenciaAccion").value),
        usu_id: parseInt(document.getElementById("usu_idAccion").value)
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarReportes();
    mostrarSeccion('lista');
}

async function eliminarReporte() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarReportes();
    mostrarSeccion('lista');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

listarReportes();
mostrarSeccion('crear');
