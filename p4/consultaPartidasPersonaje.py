from tkinter import *
import pymysql as mdb
import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os

class Aplicacion(object):
    def __init__(self, ventana, ip, user, pswd, db):

        # Datos para conectarse a la base de datos
        self.ip = ip
        self.user = user
        self.pswd = pswd
        self.db = db

        self.peticion_realizada = False
        self.path_defecto="./data/partidasPersonaje.csv"


        self.fila_actual = 0

        # Etiqueta ConsultarPartidasPersonaje
        self.etiqueta_personaje = Label(ventana, text="Consultar partidas de un personaje.")
        self.etiqueta_personaje.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        # Botón ConsultarPartidasPersonaje
        self.peticion_boton = Button(ventana, text = "Elegir personaje")
        self.peticion_boton.configure(command = self.query_personaje)
        self.peticion_boton.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1


    def query_personaje(self):
        self.ventana_personaje = Tk()
        self.ventana_personaje.wm_title("Personaje")

        #Entrada para el personaje
        self.personaje_buscado = StringVar()
        self.entrada_personaje = Entry(self.ventana_personaje,textvariable = self.personaje_buscado)
        self.entrada_personaje.grid(row = 0,column = 0, columnspan = 2)

        #Botón para el guardado
        self.boton_personaje = Button(self.ventana_personaje, text="Enviar")
        self.boton_personaje.configure(command = self.query_personaje_2)
        self.boton_personaje.grid(row = 1, column = 0, columnspan = 2)


    def query_personaje_2(self):
        #Lee el texto de la entrada
        if self.personaje_buscado.get()== "":
            messagebox.showinfo("Error", "No ha introducido ningún nombre de personaje")
            self.personaje_buscado= "W1lly"

        #Buscamos al personaje en el sistema.
        self.peticion= "SELECT identificador FROM Personaje WHERE nombre=\'"+self.personaje_buscado+"\';"
        print("Peticion: "+self.peticion)
        conexion = mdb.connect(self.ip, self.user, self.pswd, self.db)
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(self.peticion)
            rows = cursor.fetchall()

            if len(rows) == 0:
                messagebox.showinfo("Error", "No hay ningún personaje con ese nombre")
            else:
                #Obtenemos las partidas asociadas a ese personaje
                self.peticion= "SELECT par_id FROM Participa WHERE per_id=\'"+str(rows[0][0])+"\';"
                print("Peticion:" + self.peticion)
                cursor.execute(self.peticion)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    messagebox.showinfo("Error", "El personaje no tiene ninguna partida asociada")
                else:
                    self.peticion= "SELECT * FROM Partida WHERE identificador=\'"+str(rows[0][0])+"\';"
                    print("Peticion:"+self.peticion)
                    cursor.execute(self.peticion)
                    rows = cursor.fetchall()
                    if len(rows)==0:
                        messagebox.showinfo("Error", "No hay ningún universo con ese identificador")
                    else:
                        # Almacenamos la info en un DataFrame
                        self.df['identificador']=[rows[i][0] for i in range(len(rows))]
                        self.df['nombre']=[rows[i][1] for i in range(len(rows))]
                        self.df['log_fechas']=[rows[i][2] for i in range(len(rows))]
                        self.df['uni_nombre']=[rows[i][3] for i in range(len(rows))]

                        self.path_defecto="./data/ConsultarPartidasPersonaje.csv"

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
