from tkinter import *
import os
import sys

raiz = Tk()

raiz.title("Ventana de Pruebas")
raiz.resizable(True, True)
p1 = PhotoImage(file = 'icono.png')
raiz.iconphoto(True, p1)

#raiz.geometry("650x350")

raiz.config(bg="blue")

frame = Frame()
frame.pack(fill="both", expand=True)
frame.config(bg="red")
frame.config(width="650", height="350")
frame.config(bd=34)
frame.config(relief="groove")
frame.config(cursor="pirate")
raiz.mainloop()
