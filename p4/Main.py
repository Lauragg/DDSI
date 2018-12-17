from tkinter import *
import pymysql as mdb
import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os

# Definimos una clase para la interfaz
class Aplicacion(object):
    def __init__(self, ventana, ip, user, pswd, db):

        # Datos para conectarse a la base de datos
        self.ip = ip
        self.user = user
        self.pswd = pswd
        self.db = db

        self.jugador_elegido = ""
        self.df = pd.DataFrame()
        self.peticion_realizada = False

        conexion = mdb.connect(self.ip, self.user, self.pswd, self.db)
        self.cursor = conexion.cursor()

    	 # Ponemos el título a la ventana
        ventana.wm_title("Super Sistema de Información")

        # Fila actual a 0
        self.fila_actual = 0

        ''' Panel de consulta '''

        # Etiqueta ConsultarUniversos
        self.universos_etiqueta = Label(ventana, text = "Consultar universos:")
        self.universos_etiqueta.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Botón ConsultarUniversos
        self.peticion_boton = Button(ventana, text = "Mandar petición")
        self.peticion_boton.configure(command = self.query_universos)
        self.peticion_boton.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Etiqueta ConsultarPersonajesJugador
        self.universos_etiqueta = Label(ventana, text = "Consultar personajes de un jugador:")
        self.universos_etiqueta.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Botón ConsultarPersonajesJugador
        self.peticion_boton = Button(ventana, text = "Elegir jugador")
        self.peticion_boton.configure(command = self.query_jugador)
        self.peticion_boton.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Etiqueta ConsultarPartidasPersonaje
        self.etiqueta_personaje = Label(ventana, text="Consultar partidas de un personaje.")
        self.etiqueta_personaje.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Botón ConsultarPartidasPersonaje
        self.peticion_boton = Button(ventana, text = "Elegir personaje")
        self.peticion_boton.configure(command = self.query_personaje)
        self.peticion_boton.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1


        # Estado de la petición
        self.estado_peticion  = Label(ventana, text = '')
        self.estado_peticion.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Linea para separar los paneles
        canvas = Canvas(master = ventana, width = 500, height = 40)
        canvas.create_line(0, 20, 500, 20, fill = "black")
        canvas.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        ''' Panel de guardado '''

        # Etiqueta para el guardado
        self.etiqueta_guardado = Label(ventana, text = "Archivo guardado: ")
        self.etiqueta_guardado.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Entrada para el guardado
        self.texto_guardado = StringVar()
        self.entrada_guardado = Entry(ventana, textvariable = self.texto_guardado)
        self.entrada_guardado.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Botón para el guardado
        self.boton_guardado = Button(ventana, text="Guardar datos")
        self.boton_guardado.configure(command = self.guardar_csv)
        self.boton_guardado.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Etiqueta vacía
        self.etiqueta_vacia  = Label(ventana, text = '')
        self.etiqueta_vacia.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

    # Si no ha habido datos
    def ErrorNoDatos(self):
        self.estado_peticion.configure(text = "Sin datos")

    # Avisa de que la petición ha acabado
    def PeticionAcabada(self):
        self.estado_peticion.configure(text = "Acabado")
        self.peticion_realizada = True

    def RealizarPeticion(self):
        print("Peticion: " + self.peticion)
        self.cursor.execute(self.peticion)


    # Manda la petición de ConsultarUniversos a la base de datos
    def query_universos(self):
        # La petición a la base de datos
        self.peticion = "SELECT * FROM Universo;"
        self.RealizarPeticion()
        rows = self.cursor.fetchall()

        # Recuperamos la informacion
        self.df.drop(self.df.index, inplace=True)
        atributos=['nombre','genero','reglas']
        for i in range(len(atributos)):
            self.df[atributos[i]] = [rows[j][i] for j in range(len(rows))]

        # Preparamos el path para guardar la información
        self.path_defecto = "./data/universosData.csv"

        if self.df.empty:
            self.ErrorNoDatos()
        else:
            self.PeticionAcabada()

    def query_jugador(self):
        self.ventana_jugador = Tk()
        self.ventana_jugador.wm_title("Alias")

        # Entrada para el jugador
        self.entrada_nombre_jugador = Entry(self.ventana_jugador)
        self.entrada_nombre_jugador.grid(row = 0, column = 0, columnspan = 2)

        # Botón para el guardado
        self.boton_entrada = Button(self.ventana_jugador, text="Enviar")
        self.boton_entrada.configure(command = self.query_jugador_2)
        self.boton_entrada.grid(row = 1, column = 0, columnspan = 2)

    def query_jugador_2(self):
        #Limpiamos el dataframe antes de comenzar la búsqueda de datos
        self.df.drop(self.df.index, inplace=True)

        # Lee el texto de la entrada
        if self.entrada_nombre_jugador.get() == "":
            messagebox.showinfo("Error", "No ha introducido ningún nombre")
        else:
            self.jugador_elegido = self.entrada_nombre_jugador.get()

            # Buscamos al jugador en el sistema
            self.peticion = "SELECT dni FROM Jugador WHERE alias=\'" + self.jugador_elegido + "\';"
            self.RealizarPeticion()
            rows = self.cursor.fetchall()

            if len(rows) == 0:
                messagebox.showinfo("Error", "No hay ningún jugador con ese alias en el sistema")
            else:
                # Obtenemos a los personajes asociados al jugador
                self.peticion = "SELECT identificador,nombre,atributos,estado FROM Personaje WHERE jug_dni=\'" + rows[0][0] + "\';"
                self.RealizarPeticion()
                rows = self.cursor.fetchall()

                # Almacenamos la info en un DataFrame
                atributos=['identificador','nombre','atributos','estado']
                for i in range(len(atributos)):
                    self.df[atributos[i]] = [rows[j][i] for j in range(len(rows))]

        # Preparamos el path para guardar la información
        self.path_defecto = "./data/personajesDelJugador.csv"

        if self.df.empty:
            self.ErrorNoDatos()
        else:
            self.PeticionAcabada()
        self.ventana_jugador.destroy()

    def query_personaje(self):
        self.ventana_personaje = Tk()
        self.ventana_personaje.wm_title("Personaje")

        #Entrada para el personaje
        self.entrada_personaje = Entry(self.ventana_personaje)
        self.entrada_personaje.grid(row = 0,column = 0, columnspan = 2)


        #Botón para el guardado
        self.boton_personaje = Button(self.ventana_personaje, text="Enviar")
        self.boton_personaje.configure(command = self.query_personaje_2)
        self.boton_personaje.grid(row = 1, column = 0, columnspan = 2)

    def query_personaje_2(self):
        #Limpiamos el dataframe antes de comenzar la búsqueda de datos.
        self.df.drop(self.df.index, inplace=True)
        self.personaje_buscado = self.entrada_personaje.get()
        print("Entrada: "+self.entrada_personaje.get()+"\nPersonaje: "+self.personaje_buscado)
        #Lee el texto de la entrada
        if self.personaje_buscado == "":
            messagebox.showinfo("Error", "No ha introducido ningún nombre de personaje")

        else:
            #Buscamos al personaje en el sistema.
            self.peticion= "SELECT identificador FROM Personaje WHERE nombre=\'"+self.personaje_buscado+"\';"
            self.RealizarPeticion()
            rows = self.cursor.fetchall()

            if len(rows) == 0:
                messagebox.showinfo("Error", "No hay ningún personaje con ese nombre")
            else:
                #Obtenemos las partidas asociadas a ese personaje
                self.peticion= "SELECT par_id FROM Participa WHERE per_id=\'"+str(rows[0][0])+"\';"
                self.RealizarPeticion()
                rows = self.cursor.fetchall()
                if len(rows) == 0:
                    messagebox.showinfo("Error", "El personaje no tiene ninguna partida asociada")
                else:
                    self.peticion= "SELECT * FROM Partida WHERE identificador=\'"+str(rows[0][0])+"\';"
                    self.RealizarPeticion()
                    rows = self.cursor.fetchall()
                    if len(rows)==0:
                        messagebox.showinfo("Error", "No hay ningún universo con ese identificador")
                    else:
                        # Almacenamos la info en un DataFrame
                        atributos=['identificador','nombre','log_fechas','uni_nombre']
                        for i in range(len(atributos)):
                            self.df[atributos[i]] = [rows[j][i] for j in range(len(rows))]

                        self.path_defecto="./data/ConsultarPartidasPersonaje.csv"

            if self.df.empty:
                self.ErrorNoDatos()
            else:
                self.PeticionAcabada()
            self.ventana_personaje.destroy()

    def guardar_csv(self):
        if self.peticion_realizada:
            # Si no hay datos
            if self.df.empty:
                 messagebox.showinfo("Error", "No hay datos")
            else:
                if self.texto_guardado.get() == "":
                    # Path por defecto
                    self.save_loc = self.path_defecto
                else:
                    # Obtenemos la localización
                    self.save_loc = self.texto_guardado.get()

                # Sacamos el path del directorio
                self.save_dir = os.sep.join(self.save_loc.split(os.sep)[:-1])
                if os.path.isdir(self.save_dir):
                    # Verificamos que el nombre de archivo sea algo mas que '.csv'
                    if len(self.save_loc.split(os.sep)[-1]) < 5:
                        messagebox.showinfo("Error", "El path debe acabar en nombreFichero.csv")
                    # Verificamos que el archivo acaba en '.csv'
                    elif self.save_loc.split(os.sep)[-1][-4:] != '.csv':
                        messagebox.showinfo("Error", "El fichero debe acabar en nombreFichero.csv")
                    else:
                        # Guardamos la información
                        self.df.to_csv(self.save_loc)
                # Si no existe el directorio
                else:
                    messagebox.showinfo("Error", "El directorio no existe")
        else:
            messagebox.showinfo("Error", "No se ha realizado la consulta")

# Creamos la interfaz y se la pasamos a Aplicacion
def main(argv):
    # Argumentos de base de datos
    ip = argv[1]
    user = argv[2]
    pswd = argv[3]
    db = argv[4]

    # Creamos la ventana
    ventana = Tk()
    start = Aplicacion(ventana, ip, user, pswd, db)
    ventana.mainloop()

# Ejecutamos el programa
if __name__ == "__main__":
    main(sys.argv)
