DROP DATABASE IF EXISTS ddsi;
CREATE DATABASE ddsi;
USE ddsi;

DROP TABLE IF EXISTS Participa;
DROP TABLE IF EXISTS Rolea;
DROP TABLE IF EXISTS Partida;
DROP TABLE IF EXISTS Personaje;
DROP TABLE IF EXISTS Jugador;
DROP TABLE IF EXISTS Universo;

CREATE TABLE Universo (
  nombre    VARCHAR(32),
  genero    VARCHAR(32),
  reglas    VARCHAR(32),
  PRIMARY KEY (nombre)
);

CREATE TABLE Jugador (
  dni             VARCHAR(9),
  alias           VARCHAR(32),
  correo          VARCHAR(32),
  PRIMARY KEY (dni),
  UNIQUE (correo)
);

CREATE TABLE Personaje (
  identificador   INT AUTO_INCREMENT,
  nombre          VARCHAR(32) NOT NULL,
  atributos       VARCHAR(32),
  estado          BIT,
  jug_dni         VARCHAR(9),
  uni_id          VARCHAR(32),
  PRIMARY KEY (identificador),
  FOREIGN KEY (jug_dni) REFERENCES Jugador(dni),
  FOREIGN KEY (uni_id) REFERENCES Universo(nombre)
);

CREATE TABLE Partida (
  identificador   INT AUTO_INCREMENT,
  nombre          VARCHAR(32) NOT NULL,
  log_fechas      VARCHAR(32),
  uni_nombre      VARCHAR(32),
  PRIMARY KEY (identificador),
  FOREIGN KEY (uni_nombre) REFERENCES Universo(nombre)
);

CREATE TABLE Rolea (
  jug_dni   VARCHAR(9),
  par_id    INT,
  CONSTRAINT PK_Rolea PRIMARY KEY (jug_dni, par_id),
  FOREIGN KEY (jug_dni) REFERENCES Jugador(dni),
  FOREIGN KEY (par_id) REFERENCES Partida(identificador)
);

CREATE TABLE Participa (
  per_id    INT,
  par_id    INT,
  CONSTRAINT PK_Participa PRIMARY KEY (per_id, par_id),
  FOREIGN KEY (per_id) REFERENCES Personaje(identificador),
  FOREIGN KEY (par_id) REFERENCES Partida(identificador)
);
