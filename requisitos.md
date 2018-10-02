# Requisitos funcionales
## Para el subsistema de jugadores:
  - **RF1.1** Añadir un nuevo jugador: esta función registra un nuevo jugador en
  el sistema a traves de los datos del mismo proporcionados por el usuario.
  - **RF1.1** Consultar la información de un jugador: esta función registra un nuevo jugador en
  el sistema a traves de los datos del mismo proporcionados por el usuario.

  - Consultar un listado de jugadores.
  - Consultar las partidas de un jugador.
  - Consultar los personajes de un jugador.

## Para el subsistema de personajes:
  - **RF2.1** Añadir un nuevo personaje: esta fucnción registra un nuevo personaje asociado a un jugador y a un universo.
  - **RF2.2** Actualizar un personaje: Esta función se encarga de actualizar los atributos de estado de un personaje.
  - **RF2.3** Consultar la información del personaje: Esta función devuelve la información básica de un personaje.
  - **RF2.4** Consultar las partidas de un personaje: Esta función devuelve todas las partidas asociadas a un personaje concreto.
  - **RF2.5** Activar/Desactivar a un personaje: Tiene dos comportamientos, si al llamarlo el personaje se encuentra activado lo desactiva y viceversa.


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


  - **RD2.1** Datos de un personaje:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Estado (booleano)
    - Atributos de estado ( referencia a un archivo de texto donde están almacenados dichos datos).
    - Universo al que pertenece (una cadena de hasta 40 caracteres con el nombre del universo).
    - Lista de partidas en las que participa (cadena o vector con el nombre o referencia de cada una de las partidas).


  - **RD2.2** Datos de un personaje almacenado:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Estado (booleano)
    - Atributos de estado ( referencia a un archivo de texto donde están almacenados dichos datos).
    - Universo al que pertenece (una cadena de hasta 40 caracteres con el nombre del universo).
    - Lista de partidas en las que participa (cadena o vector con el nombre o referencia de cada una de las partidas).


  - **RD2.3** Confirmación por salida sobre si el personaje ha sido correctamente añadido o no.
    - Confirmación (Cadena de caracteres que indique si ha funcionado correctamente y en caso de que no indique el motivo.)


  - **RD2.4** Nuevos valores de los atributos.
    - Atributos (Cadenas de caracteres con los nuevos valores de los atributos.)


  - **RD2.5** Nuevos valores de atributos almacenados.
    - Atributos (Cadenas de caracteres con los nuevos valores de los atributos.)


  - **RD2.6** Confirmación por salida sobre si los datos han sido correctamente actualizados o no.
    - Confirmación (Cadena de caracteres que indique si ha funcionado correctamente y en caso de que no indique el motivo.)


  - **RD2.7** Acceso a datos del personaje almacenados:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Estado (booleano)
    - Atributos de estado ( referencia a un archivo de texto donde están almacenados dichos datos).
    - Universo al que pertenece (una cadena de hasta 40 caracteres con el nombre del universo).


  - **RD2.8** Salida de datos del personaje:
    - Nombre (una cadena de hasta 20 caracteres no vacía)
    - Estado (booleano)
    - Atributos de estado ( referencia a un archivo de texto donde están almacenados dichos datos).
    - Universo al que pertenece (una cadena de hasta 40 caracteres con el nombre del universo).


  - **RD2.9** Acceso a datos de partidas asociadas a un personaje almacenadas:
    - Lista de partidas en las que participa (cadena o vector con el nombre o referencia de cada una de las partidas).


  - **RD2.10** Salida de datos de partidas asociadas a un personaje:
    - Lista de partidas en las que participa (cadena o vector con el nombre o referencia de cada una de las partidas).


  - **RD2.11** Acceso al dato estado de un personaje almacenado:
    - Estado (booleano)


  - **RD2.12** Confirmación por salida sobre si el valor estado ha sido correctamente modificado o no.
    - Confirmación (Cadena de caracteres que indique si ha funcionado correctamente y en caso de que no indique el motivo.)


# Restricciones semánticas
  - **RS1.1** (**RF1.1**,**RD1.1**): Es necesario tener un mínimo de 18 años para poder registrarse.
  en el sistema.
  - **RS1.2** (**RF1.1**,**RD1.1**): Es necesario que el DNI sea correcto.
  - **RS1.3** (**RF1.1**,**RD1.1**): Es necesario que el correo sea una dirección de correo válida.
  - **RS2.1** (**RF2.1**,**RD2.1**): Es necesario que el nombres sea una cadena de caracteres no numéricos.
  - **RS2.2** (**RF2.1**,**RD2.1**): Es necesario que sea un universo existente.
  - **RS2.3** (**RF2.1**,**RD2.1**): Es necesario que todas las partidas del listado existan.
  - **RS2.4** (**RF2.1**,**RD2.1**): Es necesario que los atributos actualizados sean válidos y concuerden con el universo asociado.
  - **RS2.5** (**RF2.2**,**RD2.4**): Es necesario que los atributos actualizados sean válidos y concuerden con el universo asociado.


RF | Entrada | Manejo | Salida
-- |
RF2.1 | RD2.1 | RD2.2 | RD2.3
RF2.2 | RD2.4 | RD2.5 | RD2.6
RF2.3 |  | RD2.7 | RD2.8
RF2.4 |  | RD2.9 | RD2.10
RF2.5 |  | RD2.11 | RD2.12

RD | Entrada | Manejo | Salida
-- |
RD2.1 | RF2.1 |  |
RD2.2 |  | RF2.1 |
RD2.3 |  |  | RD2.1
RD2.4 | RF2.2 |  |
RD2.5 |  | RD2.2 |
RD2.6 |  |  | RD2.2
RD2.7 |  | RD2.3 |
RD2.8 |  |  | RD2.3
RD2.9 |  | RD2.4 |
RD2.10 |  |  | RD2.4
RD2.11 |  | RD2.5 |
RD2.12 |  |  | RD2.5

RS | RF | RD
--|
RS2.1 | RF2.1 | RD2.1
RS2.2 | RF2.1 | RD2.1
RS2.3 | RF2.1 | RD2.1
RS2.4 | RF2.1 | RD2.1
RS2.5 | RF2.2 | RD2.4






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
