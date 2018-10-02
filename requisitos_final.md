# Subsistema de Jugadores

# Requisitos funcionales
## Para el subsistema de jugadores:
  - **RF1.1** Añadir un nuevo jugador: esta función registra un nuevo jugador en
  el sistema a traves de los datos del mismo proporcionados por el usuario.

  - **RF1.2** Consultar la información de un jugador: esta función muestra la información
  del jugador asociado al DNI recibido por el usuario.

  - **RF1.3** Consultar un listado de jugadores: esta función muestra los alias
  de todos los jugadores almacenados en el sistema.

  - **RF1.4** Consultar las partidas de un jugador: esta función muestra las partidas
  del jugador asociado al Alias recibido por entrada.

  - **RF1.5** Consultar los personajes de un jugador: esta función muestra los personajes del jugador asociado al Alias recibido por entrada.

## Para el subsistema de partidas y universos:
  - **RF3.1** Añadir un nuevo universo: esta función registra un nuevo universo
  en el sistema a través de los datos del mismo proporcionados por el usuario.

  - **RF3.2** Crear una nueva partida: esta función registra una nueva partida
  en el sistema a través de los datos del mismo proporcionados por el usuario:
  el nombre y la selección del universo sobre el que se desarrolla dada por la
  lista disponible de universos, y después la selección de personajes dada
  por la lista disponible de personajes de ese universo escogido.

  - **RF3.3** Consultar listado de partidas: esta función devuelve todas las partidas existentes en el sistema.

  - **RF3.4** Consultar listado de universos: esta función devuelve todas los universos existentes en el sistema.

  - **RF.3.5** Consultar los datos de una partida: esta función devuelve toda
  la información de una partida, escogida por el usuario de la lista de partidas.

  - **RF3.6** Consultar listado de las partidas de un universo: esta función
  devuelve todas las partidas asociadas a un universo, escogido por el usuario
  de la lista de universos existentes.

# Requisitos de datos
## Para el subsistema de jugadores:
  - **RD1.1** Datos de un jugador:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)
    - Edad (dato numérico)

  - **RD1.2** Datos de un jugador a almacenar:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)

  - **RD1.3** Mensaje de correcto funcinamiento:
    - Mensaje (una cadena de hasta 50 caracteres no vacía)

  - **RD1.4** DNI de un jugador:
    - DNI (una cadena de 9 caracteres)

  - **RD1.5** Datos de un jugador almacenados:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)
    - Lista de personajes asociados al jugador (cadena de caracteres)

  - **RD1.6** Datos de un jugador mostrados por salida:
    - Alias (una cadena de hasta 20 caracteres no vacía)
    - DNI (una cadena de 9 caracteres)
    - Correo (cadena de caracteres de hasta 40 caracteres)
    - Lista de personajes asociados al jugador (cadena de caracteres)

  - **RD1.7** Listado de jugadores almacenados:
    - Cadena de Alias de personajes (cadenas no vacías de hasta 20 caracteres)

  - **RD1.8** Listado de jugadores mostrado por salida:
    - Cadena de Alias de personajes (cadenas no vacías de hasta 20 caracteres)

  - **RD1.9** Alias del jugador:
    - Alias (cadena no vacía de hasta 20 caracteres)

  - **RD1.10** Listado de partidas almacenadas:
    - Listado de partidas

  - **RD1.11** Listado de partidas mostradas por salida:
    - Listado de partidas

  - **RD1.12** Alias del jugador:
    - Alias (cadena no vacía de hasta 20 caracteres)

  - **RD1.13** Listado de personajes almacenado:
    - Listado de personajes

  - **RD1.14** Listado de personajes mostradas por salida:
    - Listado de personajes

## Para el subsistema de partidas y universos:

  - **RD3.1** Datos de un universo:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Género (una cadena de hasta 40 caracteres no vacía)
    - Reglas del universo (serie de campos diversos rellenados por el usuario)

  - **RD3.2** Datos de un universo almacenados:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Género (una cadena de hasta 40 caracteres no vacía)
    - Reglas del universo (serie de campos diversos)
    - Lista de personajes (lista de los personajes que pertenecen al universo)
    - Lista de partidas (lista de partidas que utilizan al universo)

  - **RD3.3** Mensaje de salida de un universo:
    - Mensaje (texto de confirmación que todo ha sido correcto o si ha habido
    algún error al crear el universo)

  - **RD3.4** Datos de una partida:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Universo (universo que se ha seleccionado donde se desarrolla la partida)
    - Personajes (lista de personajes del universo seleccionado que van a jugar)

  - **RD3.5** Datos de una partida almacenada:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Universo (universo que se ha seleccionado donde se desarrolla la partida)
    - Personajes (lista de personajes del universo seleccionado que van a jugar)
    - Log de fechas (listado de fechas, empezando con la fecha de creación de
    la partida, y creando una entrada cada vez que se pausa la partida)

  - **RD3.6** Mensaje de salida de una partida:
    - Mensaje (texto de confirmación que todo ha sido correcto o si ha habido
    algun error al crear la partida)

  - **RD3.7** Datos de consulta de listado de partidas almacenados:
    - Partidas (las partidas que hay en la base de datos)

  - **RD3.8** Salida de listado de partidas:
    - Lista de partidas (lista de partidas que hay en la base de datos)

  - **RD3.9** Datos de consulta de listado de universos almacenados:
    - Universos (los universos que hay en la base de datos)

  - **RD3.10** Salida de listado de universos:
    - Lista de universos (lista de universos que hay en la base de datos)

  - **RD3.11** Datos de consulta de datos de una partida:
    - Partida (la partida que ha escogido el usuario para consultar su
    información)

  - **RD3.12** Datos de consulta de datos de una partida almacenados:
    - Partidas (todas las partidas que hay en la base de datos)
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Universo (universo que se ha seleccionado donde se desarrolla la partida)
    - Personajes (lista de personajes del universo seleccionado que van a jugar)
    - Log de fechas (listado de fechas, empezando con la fecha de creación de
    la partida, y creando una entrada cada vez que se pausa la partida)

  - **RD3.13** Salida de datos de una partida:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Universo (universo que se ha seleccionado donde se desarrolla la partida)
    - Personajes (lista de personajes del universo seleccionado que van a jugar)
    - Log de fechas (listado de fechas, empezando con la fecha de creación de
    la partida, y creando una entrada cada vez que se pausa la partida)

  - **RD3.14** Datos de consulta listado de las partidas de un universo:
    - Universo (universo escogido por el usuario para consultar sus partidas)

  - **RD3.15** Datos de consulta listado de las partidas de un universo almacenados:
    - Universos (todos los universos que hay en la base de datos)
    - Partidas (todas las partidas que hay en la base de datos)

  - **RD3.16** Salida de listado de partidas de un universo:
    - Lista de partidas (lista de partidas que están desarrolladas en el
    universo escogido para la consulta)


# Restricciones semánticas
## Para el subsistema de jugadores:

  - **RS1.1** (**RF1.1**,**RD1.1**): Es necesario tener un mínimo de 18 años para poder registrarse.
  en el sistema.

  - **RS1.2** (**RF1.1**,**RD1.1**): Es necesario que el DNI sea un DNI válido y que no esté ya en el sistema.

  - **RS1.3** (**RF1.1**,**RD1.1**): Es necesario que el correo sea una dirección de correo válida.

  - **RS1.4** (**RF1.2**,**RD1.4**): Es necesario que el DNI sea un DNI válido.

  - **RS1.5** (**RF1.4**,**RD1.9**): Es necesario que el Alias esté ya asociado a un jugador.

  - **RS1.6** (**RF1.5**,**RD1.12**): Es necesario que el Alias esté ya asociado a un jugador.

## Para el subsistema de partidas y universos:

  - **RS3.1** (**RF3.1**,**RD3.1**): Es necesario que las reglas del universo
  tengan valores válidos.

  - **RS3.2** (**RF3.2**, **RD3.4**): Es necesario que exista al menos un
  universo, y este mismo tenga al menos un personaje.


# Tablas de asociaciones

## Tabla de requisitos de datos

RD  | Entrada | Manejo | Salida
-- | --
RD1.1 | RF1.1 |  |
RD1.2 |  | RF1.1 |
RD1.3 |  |  | RF1.1
RD1.4 | RF1.2 |  |
RD1.5 |  |  RF1.2 |
RD1.6 |  |  |  RF1.2
RD1.7 |  |  RF1.3 |
RD1.8 |  |  | RF1.3
RD1.9 | RF1.4 |  |
RD1.10 |  | RF1.4 |
RD1.11 |  |  | RF1.4
RD1.12 | RF1.5 |  |
RD1.13 |  | RF1.5 |
RD1.14 |  |  | RF1.5
RD3.1 | RF3.1 |  |
RD3.2 |  | RF3.1 |
RD3.3 |  |  | RF3.1
RD3.4 | RF3.2 |  |
RD3.5 |  |  RF3.2 |
RD3.6 |  |  |  RF3.2
RD3.7 |  |  RF3.3 |
RD3.8 |  |  | RF3.3
RD3.9 |  | RF3.4 |
RD3.10 |  |  | RF3.4
RD3.11 | RF3.5 |  |
RD3.12 |  | RF3.5 |
RD3.13 |  |  | RF3.5
RD3.14 | RF3.6 |  |
RD3.15 |  |  RF3.6 |
RD3.16 |  |  |  RF3.6

## Tabla de requisitos funcionales

RF  | Entrada | Manejo | Salida
-- | --
RF1.1 | RD1.1 | RD1.2 | RD1.3
RF1.2 | RD1.4 | RD1.5 | RD1.6
RF1.3 |  | RD1.7 | RD1.8
RF1.4 | RD1.9 | RD1.10 | RD1.11
RF1.5 | RD1.12 | RD1.13 | RD1.14
RF3.1 | RD3.1 | RD3.1 | RD3.3
RF3.2 | RD3.4 | RD3.5 | RD3.6
RF3.3 |  | RD3.7 | RD3.8
RF3.4 |  | RD3.9 | RD3.10
RF3.5 | RD3.11 | RD3.12 | RD3.13
RF3.6 | RD3.14 | RD3.15 | RD3.16

## Tabla de restricciones semánticas

RS  | RF | RD
-- | --
RS1.1 | RF1.1 | RD1.1
RS1.2 | RF1.1 | RD1.1
RS1.3 | RF1.1 | RD1.1
RS1.4 | RF1.2 | RD1.4
RS1.5 | RF1.4 | RD1.9
RS1.6 | RF1.5 | RD1.12
RS3.1 | RF3.1 | RD3.1
RS3.2 | RF3.2 | RD3.4
