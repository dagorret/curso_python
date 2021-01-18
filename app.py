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
mi_frame = Frame(root)
mi_frame.pack()

cuadro_id = Entry(mi_frame)
cuadro_id.grid(row=0, column=1, padx=6, pady=6)

cuadro_nombre = Entry(mi_frame)
cuadro_nombre.grid(row=1, column=1, padx=6, pady=6)
cuadro_nombre.config(fg="red", justify="right")

cuadro_pass = Entry(mi_frame)
cuadro_pass.grid(row=2, column=1, padx=6, pady=6)
cuadro_pass.config(show="*")

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=3, column=1, padx=6, pady=6)

cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=4, column=1, padx=6, pady=6)

cuadro_texto = Text(mi_frame, width=16, height=5)
cuadro_texto.grid(row=5, column=1, padx=6, pady=6)
scroll_ver = Scrollbar(mi_frame, command=cuadro_texto.yview)
scroll_ver.grid(row=5, column=2, sticky="nsew")
cuadro_texto.config(yscrollcommand = scroll_ver.set)

# Label
l_id = Label(mi_frame, text = "Id:")
l_id.grid(row=0, column=0, sticky="e", padx=6, pady=6)

l_nombre = Label(mi_frame, text = "Nombre:")
l_nombre.grid(row=1, column=0, sticky="e", padx=6, pady=6)

l_pass = Label(mi_frame, text = "Password:")
l_pass.grid(row=2, column=0, sticky="e", padx=6, pady=6)

l_apellido = Label(mi_frame, text = "Apellido:")
l_apellido.grid(row=3, column=0, sticky="e", padx=6, pady=6)

l_id = Label(mi_frame, text = "Id:")
l_id.grid(row=4, column=0, sticky="e", padx=6, pady=6)

l_texto = Label(mi_frame, text = "Comentarios:")
l_texto.grid(row=5, column=0, sticky="e", padx=6, pady=6)

# Botones
b_frame = Frame(root)
b_frame.pack()

btn_crear = Button(b_frame, text="Crear")
btn_crear.grid(row=0, column=0, sticky="e", padx=6, pady=6)


btn_leer = Button(b_frame, text="Leer")
btn_leer.grid(row=0, column=1, sticky="e", padx=6, pady=6)


btn_actualizar = Button(b_frame, text="Actualizar")
btn_actualizar.grid(row=0, column=2, sticky="e", padx=6, pady=6)


btn_borrar = Button(b_frame, text="Borrar")
btn_borrar.grid(row=0, column=3, sticky="e", padx=6, pady=6)

root.mainloop()
