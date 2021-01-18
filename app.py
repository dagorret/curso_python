from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# Funciones

def conexion():
    mi_conexion = sqlite3.connect("app.db")
    cursor = mi_conexion.cursor()

    try:
        cursor.execute('''
            CREATE TABLE datausuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50),
            password VARCHAR(50),
            apellido VARCHAR(10),
            direccion VARCHAR(50),
            comentarios VARCHAR(100)
            )
            ''')
        messagebox.showinfo("BBDD", "La base de datos fue creada con exito")
    except:
        messagebox.showwarning("¡Atención!", "La base de datos ya existe")

def salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación")
    if valor == "yes":
        root.destroy()

def borrar():
    v_id.set("")
    v_nombre.set("")
    v_apellido.set("")
    v_direccion.set("")
    v_pass.set("")
    cuadro_texto.delete(1.0, END)

def crear():
    mi_conexion = sqlite3.connect("app.db")
    cursor = mi_conexion.cursor()
    comentario = cuadro_texto.get("1.0", END)
    sql = f"INSERT INTO datausuarios VALUES(NULL, '{v_nombre.get()}', '{v_pass.get()}', '{v_apellido.get()}', '{v_direccion.get()}', '{comentario}')"
    cursor.execute(sql)
    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado")

def leer():
    mi_conexion = sqlite3.connect("app.db")
    cursor = mi_conexion.cursor()
    cursor.execute("SELECT * FROM datausuarios WHERE id=" + v_id.get() )
    datos = cursor.fetchall()

    for u in datos:
        v_id.set(u[0])
        v_nombre.set(u[1])
        v_pass.set(u[2])
        v_apellido.set(u[3])
        v_direccion.set(u[4])
        cuadro_texto.insert(1.0, u[5])

def actualizar():
    mi_conexion = sqlite3.connect("app.db")
    cursor = mi_conexion.cursor()
    comentario = cuadro_texto.get("1.0", END)
    sql = f"UPDATE datausuarios SET nombre = '{v_nombre.get()}', password = '{v_pass.get()}', apellido ='{v_apellido.get()}', direccion ='{v_direccion.get()}', comentarios ='{comentario}' WHERE id='{v_id.get()}'"
    cursor.execute(sql)
    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro se ha actualizado")

# Menu
barramenu = Menu(root)
root.config(menu = barramenu, width=300, height=300)

bbdd_menu = Menu(barramenu, tearoff=0)
bbdd_menu.add_command(label = "Conectar", command = conexion)
bbdd_menu.add_command(label = "Salir", command = salir)

borrar_menu = Menu(barramenu, tearoff=0)
borrar_menu.add_command(label = "Borrar Campos", command=borrar)


crud_menu = Menu(barramenu, tearoff=0)
crud_menu.add_command(label = "Crear", command=crear)
crud_menu.add_command(label = "Leer", command = leer)
crud_menu.add_command(label = "Actualizar", command=actualizar)
crud_menu.add_command(label = "Borrar")


ayuda_menu = Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label = "Licencia")
ayuda_menu.add_command(label = "Acerca de ...")

barramenu.add_cascade(label="BBDD", menu=bbdd_menu)
barramenu.add_cascade(label="Borrar", menu=borrar_menu)
barramenu.add_cascade(label="CRUD", menu=crud_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)

# Campos
    #variables
v_id = StringVar()
v_nombre = StringVar()
v_apellido = StringVar()
v_pass = StringVar()
v_direccion = StringVar()

mi_frame = Frame(root)
mi_frame.pack()

cuadro_id = Entry(mi_frame, textvariable=v_id)
cuadro_id.grid(row=0, column=1, padx=6, pady=6)

cuadro_nombre = Entry(mi_frame, textvariable=v_nombre)
cuadro_nombre.grid(row=1, column=1, padx=6, pady=6)
cuadro_nombre.config(fg="red", justify="right")

cuadro_pass = Entry(mi_frame, textvariable=v_pass)
cuadro_pass.grid(row=2, column=1, padx=6, pady=6)
cuadro_pass.config(show="*")

cuadro_apellido = Entry(mi_frame, textvariable=v_apellido)
cuadro_apellido.grid(row=3, column=1, padx=6, pady=6)

cuadro_direccion = Entry(mi_frame, textvariable=v_direccion)
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

l_id = Label(mi_frame, text = "Dirección:")
l_id.grid(row=4, column=0, sticky="e", padx=6, pady=6)

l_texto = Label(mi_frame, text = "Comentarios:")
l_texto.grid(row=5, column=0, sticky="e", padx=6, pady=6)

# Botones
b_frame = Frame(root)
b_frame.pack()

btn_crear = Button(b_frame, text="Crear", command=crear)
btn_crear.grid(row=0, column=0, sticky="e", padx=6, pady=6)


btn_leer = Button(b_frame, text="Leer", command = leer)
btn_leer.grid(row=0, column=1, sticky="e", padx=6, pady=6)


btn_actualizar = Button(b_frame, text="Actualizar", command=actualizar)
btn_actualizar.grid(row=0, column=2, sticky="e", padx=6, pady=6)


btn_borrar = Button(b_frame, text="Borrar")
btn_borrar.grid(row=0, column=3, sticky="e", padx=6, pady=6)

root.mainloop()
