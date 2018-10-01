# Requisitos funcionales
## Para el subsistema de jugadores:
  - **RF1.1** Añadir un nuevo jugador: esta función registra un nuevo jugador en
  el sistema a traves de los datos del mismo proporcionados por el usuario.
  - **RF1.1** Consultar la información de un jugador: esta función registra un nuevo jugador en
  el sistema a traves de los datos del mismo proporcionados por el usuario.

  -.
  - Consultar un listado de jugadores.
  - Consultar las partidas de un jugador.
  - Consultar los personajes de un jugador.

# Requisitos de datos
  - **RD1.1** Datos de un jugador:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)
    - Edad (dato numérico)
  - **RD1.2** Datos de un jugador a almacenar:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)

# Restricciones semánticas
  - **RS1.1** (**RF1.1**,**RD1.1**): Es necesario tener un mínimo de 18 años para poder registrarse.
  en el sistema.
  - **RS1.2** (**RF1.1**,**RD1.1**): Es necesario que el DNI sea correcto.
  - **RS1.3** (**RF1.1**,**RD1.1**): Es necesario que el correo sea una dirección de correo válida.

- Para el subsistema de personajes:
  - Añadir un personaje.
  - Actualizar un personaje.
  - Consultar la información del personaje.
  - Consultar las partidas de un personaje.
  - Eliminar a un personaje.


- Para el subsistema de universos y partidas:
  - Añadir un nuevo universo.
  - Crear una nueva partida.
  - Consultar listado de partidas.
  - Consultar listado de universos.
  - Consultar los datos de una partida.
  - Consultar listado de las partida de un universo.

Almacenamos la siguiente información:

  - Jugador:
    - Alias
    - DNI
    - Correo
    - Lista de personajes

  - Personaje:
    - Nombre.
    - Atributos de estado.
    - Universo al que pertenece.
    - Lista de partidas en las que participa.

      Nota: el personaje recibe una lista a completar de
atributos por parte del universo.

  - Universo:
    - Nombre
    - Género(s)
    - Lista de personajes
    - Lista de partidas del universo
    - Reglas del universo

  - Partida:
    - Nombre
    - Log de fechas
    - Lista de personajes que participan
    - Universo en el que se desarrolla
