from datetime import datetime

class ReporteDTO:
    def __init__(self, tip_id, rep_descripcion, rep_url_imagen, rep_nivel_incidencia, usu_id, id=None):
        self.id = id
        self.tip_id = tip_id
        self.rep_descripcion = rep_descripcion
        self.rep_url_imagen = rep_url_imagen
        self.rep_nivel_incidencia = rep_nivel_incidencia
        self.usu_id = usu_id



    def __str__(self):
        return (f"ReporteDTO(rep_id={self.rep_id}, tip_id={self.tip_id}, "
                f"rep_descripcion='{self.rep_descripcion}', rep_url_imagen='{self.rep_url_imagen}', "
                f"rep_nivel_incidencia={self.rep_nivel_incidencia}, usu_id={self.usu_id}, fecha={self.fecha})")
