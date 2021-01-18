from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# Menu
barramenu = Menu(root)
root.config(menu = barramenu, width=300, height=300)

bbdd_menu = Menu(barramenu, tearoff=0)
bbdd_menu.add_command(label = "Conectar")
bbdd_menu.add_command(label = "Salir")

borrar_menu = Menu(barramenu, tearoff=0)
borrar_menu.add_command(label = "Borrar Campos")


crud_menu = Menu(barramenu, tearoff=0)
crud_menu.add_command(label = "Crear")
crud_menu.add_command(label = "Leer")
crud_menu.add_command(label = "Actualizar")
crud_menu.add_command(label = "Borrar")


ayuda_menu = Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label = "Licencia")
ayuda_menu.add_command(label = "Acerca de ...")

barramenu.add_cascade(label="BBDD", menu=bbdd_menu)
barramenu.add_cascade(label="Borrar", menu=borrar_menu)
barramenu.add_cascade(label="CRUD", menu=crud_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)

# Campos


root.mainloop()
