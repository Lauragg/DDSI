CREATE TABLE Universo (
  nombre    VARCHAR2(32) PRIMARY KEY,
  genero    VARCHAR2(32),
  reglas    VARCHAR2(32)
);

CREATE TABLE Jugador (
  dni             VARCHAR2(9) PRIMARY KEY,
  alias           VARCHAR2(32),
  correo          VARCHAR2(32) UNIQUE
);

CREATE TABLE Personaje (
  identificador   NUMBER PRIMARY KEY,
  nombre          VARCHAR2(32) NOT NULL,
  atributos       VARCHAR2(32),
  estado          BIT,
  jug_id          NUMBER FOREIGN KEY REFERENCES Jugador(identificador)
);

CREATE TABLE Partida (
  identificador   NUMBER PRIMARY KEY,
  nombre          VARCHAR2(32) NOT NULL,
  log_fechas      VARCHAR2(32),
  uni_nombre      VARCHAR2(32) FOREIGN KEY REFERENCES Universo(nombre)
);

CREATE TABLE Rolea (
  jug_id    NUMBER FOREIGN KEY REFERENCES Jugador(identificador),
  par_id    NUMBER FOREIGN KEY REFERENCES Partida(identificador),
  CONSTRAINT PK_Rolea PRIMARY KEY (jug_id, par_id)
);

CREATE TABLE Participa (
  per_id    NUMBER FOREIGN KEY REFERENCES Personaje(identificador),
  par_id    NUMBER FOREIGN KEY REFERENCES Partida(identificador),
  CONSTRAINT PK_Participa PRIMARY KEY (per_id, par_id)
);
