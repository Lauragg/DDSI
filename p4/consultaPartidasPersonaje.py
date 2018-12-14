import tkinter as tk
import sys

class App(tk.Frame):
    def __init__(self, ip, user, pswd, db, master=None):
        super().__init__(master)
        self.pack()

        #Inicializamos los datos para conectarnos la base de Datos
        self.ip=ip
        self.user = user
        self.pswd=pswd
        self.db=db

        self.peticion_realizada= False
        self.path_defecto="./data/partidasPersonaje.csv"



def main(argv):
    # Creamos la aplicación
    myapp = App(argv[1],argv[2],argv[3],argv[4])

    #
    # Estos son los metodos que llaman a la clase controladora de la ventana.
    #
    myapp.master.title("Consulta de las partidas asociadas a un personaje.")
    myapp.master.maxsize(1000, 400)

    # Iniciamos el programa
    myapp.mainloop()

# Ejecutamos el programa
if __name__ == "__main__":
    main(sys.argv)
