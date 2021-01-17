from tkinter import *
import os
import sys

raiz = Tk()

raiz.title("Ventana de Pruebas")
raiz.resizable(True, False)
p1 = PhotoImage(file = 'icono.png')
raiz.iconphoto(True, p1)

raiz.geometry("650x350")

raiz.config(bg="blue")
raiz.mainloop()
