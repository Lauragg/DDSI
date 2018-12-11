USE ddsi;

INSERT INTO Universo VALUES ("Universo 1", "SciFi", "reglas1.txt");
INSERT INTO Universo VALUES ("Universo 2", "Fantasía", "reglas2.txt");
INSERT INTO Universo VALUES ("Universo 3", "Medieval", "reglas3.txt");

INSERT INTO Jugador VALUES ("12345678A", "Willyrex", "willyrex@hotmail.com");
INSERT INTO Jugador VALUES ("12345679B", "Rubius", "rubius@hotmail.es");
INSERT INTO Jugador VALUES ("12345672Z", "Yellowmellow", "yellow@gmail.com");

INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("W1lly", "Magia", 0, "12345678A", "Universo 1");
INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("W2lly", "Agilidad", 1, "12345678A", "Universo 2");
INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("W3lly", "Fuerza", 0, "12345678A", "Universo 1");

INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("Rub1us", "Alquimia", 0, "12345679B", "Universo 2");
INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("Rubi2s", "Arquería", 0, "12345679B", "Universo 3");

INSERT INTO Personaje (nombre, atributos, estado, jug_dni, uni_id)
  VALUES ("Yel1ow", "Sigilo", 1, "12345672Z", "Universo 3");

INSERT INTO Partida (nombre, log_fechas, uni_nombre)
  VALUES ("Partida 1", "log1", "Universo 1");
INSERT INTO Partida (nombre, log_fechas, uni_nombre)
  VALUES ("Partida 2", "log2", "Universo 2");
INSERT INTO Partida (nombre, log_fechas, uni_nombre)
  VALUES ("Partida 3", "log3", "Universo 2");
INSERT INTO Partida (nombre, log_fechas, uni_nombre)
  VALUES ("Partida 4", "log4", "Universo 3");

INSERT INTO Rolea VALUES ("12345678A", 1);
INSERT INTO Rolea VALUES ("12345678A", 2);
INSERT INTO Rolea VALUES ("12345679B", 2);
INSERT INTO Rolea VALUES ("12345679B", 3);
INSERT INTO Rolea VALUES ("12345679B", 4);
INSERT INTO Rolea VALUES ("12345672Z", 4);

INSERT INTO Participa VALUES (1, 1);
INSERT INTO Participa VALUES (2, 2);
INSERT INTO Participa VALUES (4, 2);
INSERT INTO Participa VALUES (5, 3);
INSERT INTO Participa VALUES (6, 4);
