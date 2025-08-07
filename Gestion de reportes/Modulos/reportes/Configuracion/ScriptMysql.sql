CREATE TABLE IF NOT EXISTS entidad_externa (
  ent_id INT AUTO_INCREMENT PRIMARY KEY,
  ent_nombre VARCHAR(100) NOT NULL,
  ent_contacto VARCHAR(100),
  ent_correo VARCHAR(100),
  ent_telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS localidad (
  loc_id INT AUTO_INCREMENT PRIMARY KEY,
  loc_descripcion VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS sector (
  sec_id INT AUTO_INCREMENT PRIMARY KEY,
  loc_id INT NOT NULL,
  sec_direccion VARCHAR(255) NOT NULL,
  FOREIGN KEY (loc_id) REFERENCES localidad(loc_id)
);

CREATE TABLE IF NOT EXISTS moderador (
  mod_id INT AUTO_INCREMENT PRIMARY KEY,
  mod_nombre VARCHAR(50) NOT NULL,
  mod_apellido VARCHAR(50) NOT NULL,
  mod_correo VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS tipo_reporte (
  tip_id INT AUTO_INCREMENT PRIMARY KEY,
  tip_descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
  usu_id INT AUTO_INCREMENT PRIMARY KEY,
  usu_nombre VARCHAR(50) NOT NULL,
  usu_apellido VARCHAR(50) NOT NULL,
  sec_id INT NOT NULL,
  usu_correo VARCHAR(80) NOT NULL,
  FOREIGN KEY (sec_id) REFERENCES sector(sec_id)
);

CREATE TABLE IF NOT EXISTS reporte (
  rep_id INT AUTO_INCREMENT PRIMARY KEY,
  tip_id INT NOT NULL,
  rep_descripcion VARCHAR(255) NOT NULL,
  rep_url_imagen VARCHAR(255) NOT NULL,
  rep_nivel_incidencia INT NOT NULL,
  usu_id INT NOT NULL,
  FOREIGN KEY (tip_id) REFERENCES tipo_reporte(tip_id),
  FOREIGN KEY (usu_id) REFERENCES usuario(usu_id)
);

CREATE TABLE IF NOT EXISTS solucion (
  sol_id INT AUTO_INCREMENT PRIMARY KEY,
  rep_id INT NOT NULL,
  mod_id INT NOT NULL,
  ent_id INT,
  sol_fecha DATE NOT NULL,
  sol_descripcion TEXT NOT NULL,
  FOREIGN KEY (rep_id) REFERENCES reporte(rep_id),
  FOREIGN KEY (mod_id) REFERENCES moderador(mod_id),
  FOREIGN KEY (ent_id) REFERENCES entidad_externa(ent_id)
);