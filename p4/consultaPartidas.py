# De momento no se usan todas las librerias

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
    def __init__(self, ventana):
    	 # Ponemos el título a la ventana
        ventana.wm_title("Ventana BaseDatos")

        # Fila actual a 0
        self.current_row=0

        '''Query Panel'''
        #Run tag field
        self.runtag_label = Label(ventana, text= "Consultar universos:")
        self.runtag_label.grid(row=self.current_row,column=0)
        self.current_row += 1



        #Send Query button
        self.query_button = Button(ventana, text="Send Query")
        #self.query_button.command=self.sendQuery
        self.query_button.grid(row=self.current_row,column=0,columnspan=2)
        self.current_row += 1

        #Query status
        self.querystatus  = Label(ventana, text='')
        self.querystatus.grid(row=self.current_row,column=0,columnspan=2)
        self.current_row += 1



#Creamos la interfaz y se la pasamos a la Aplicacion
def main():
	ventana = Tk()
	start = Aplicacion(ventana)
	ventana.mainloop()

#Run the main function
if __name__ == "__main__":
    main()
