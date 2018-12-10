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

        self.peticion_realizada = False
        self.path_defecto = "./data/universosData.csv"

    	 # Ponemos el título a la ventana
        ventana.wm_title("Ventana BaseDatos")

        # Fila actual a 0
        self.fila_actual = 0

        ''' Panel de consulta '''
        # Consultar universos etiqueta
        self.universos_etiqueta = Label(ventana, text = "Consultar universos:")
        self.universos_etiqueta.grid(row = self.fila_actual, column = 0, columnspan = 2)
        self.fila_actual += 1

        #Enviar petición botón
        self.peticion_boton = Button(ventana, text = "Mandar petición")
        self.peticion_boton.configure(command = self.mandar_query)
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

    # Manda la petición a la base de datos
    def mandar_query(self):
        # La petición a la base de datos
        self.peticion = "SELECT * FROM Universo;"
        # Conexión a la base de datos (ip, usuario, contraseña, nombre baseDatos)
        conexion = mdb.connect(self.ip, self.user, self.pswd, self.db)

        with conexion:
            # Tomamos el cursor de la conexión con la base de datos
            cursor = conexion.cursor()
            # Ejecutamos la petición
            cursor.execute(self.peticion)
            # Numero de filas
            rows = cursor.fetchall()

            # Recuperamos la informacion
            self.df = pd.DataFrame()
            self.df['nombre'] = [rows[i][0] for i in range(len(rows))]
            self.df['genero'] = [rows[i][1] for i in range(len(rows))]
            self.df['reglas'] = [rows[i][2] for i in range(len(rows))]

        if self.df.empty:
            #Si no ha habido datos
            self.estado_peticion.configure(text = "Sin datos")
        else:
            # Avisa de que la petición ha acabado
            self.estado_peticion.configure(text = "Acabado")
        self.peticion_realizada = True

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
