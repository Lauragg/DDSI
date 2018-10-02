# Requisitos funcionales
-------------------------------------------------------------------------------

  - **RF3.1** Añadir un nuevo universo: esta función registra un nuevo universo
  en el sistema a través de los datos del mismo proporcionados por el usuario.

  - **RF3.2** Crear una nueva partida: esta función registra una nueva partida
  en el sistema a través de los datos del mismo proporcionados por el usuario:
  el nombre y la selección del universo sobre el que se desarrolla dada por la
  lista disponible de universos, y después la selección de personajes dada
  por la lista disponible de personajes de ese universo escogido.

  - **RF3.3** Consultar listado de partidas: esta función devuelve todas las
  partidas existentes en la base de datos.

  - **RF3.4** Consultar listado de universos: esta función devuelve todas los
  universos existentes en la base de datos.

  - **RF.3.5** Consultar los datos de una partida: esta función devuelve toda
  la información de una partida, escogida por el usuario de la lista de partidas
  existentes por el usuario.

  - **RF3.6** Consultar listado de las partidas de un universo: esta función
  devuelve todas las partidas asociadas a un universo, escogido por el usuario
  de la lista de universos existentes.

# Requisitos de datos
-------------------------------------------------------------------------------

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
-------------------------------------------------------------------------------

  - **RS3.1** (**RF3.1**,**RD3.1**): Es necesario que las reglas del universo
  tengan valores válidos.

  - **RS3.2** (**RF3.2**, **RD3.4**): Es necesario que exista al menos un
  universo, y este mismo tenga al menos un personaje.
