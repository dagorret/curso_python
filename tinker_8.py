from tkinter import *
from tkinter import messagebox

root = Tk()

def InfoAdicional():
    messagebox.showinfo("Procesador", "Procesador versión 1.0")

def InfoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def Salir():
    #valor = messagebox.askquestion("Salir", "¿Desea salir de la apliacación?")
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la apliacación?")
    if valor:
        root.destroy()

def Cerrar():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar")
    if not valor:
        root.destroy()

barramenu = Menu(root)
root.config(menu=barramenu, width = 300, height=300)

archivo_menu = Menu(barramenu, tearoff=0)
archivo_menu.add_command(label = "Nuevo")
archivo_menu.add_command(label = "Guardar")
archivo_menu.add_command(label = "Guardar como")
archivo_menu.add_separator()
archivo_menu.add_command(label = "Cerrar", command=Cerrar)
archivo_menu.add_command(label = "Salir", command=lambda:Salir())

archivo_edicion_menu = Menu(barramenu, tearoff = 0)
archivo_edicion_menu.add_command(label = "Copiar")
archivo_edicion_menu.add_command(label = "Cortar")
archivo_edicion_menu.add_command(label = "Pegar")
archivo_herramientas_menu = Menu(barramenu)
archivo_ayuda = Menu(barramenu, tearoff = 0)
archivo_ayuda.add_command(label = "Licencia", command=InfoLicencia)
archivo_ayuda.add_command(label = "Acerca de ..", command=InfoAdicional)

barramenu.add_cascade(label = "Archivo", menu = archivo_menu)
barramenu.add_cascade(label = "Edición", menu = archivo_edicion_menu)
barramenu.add_cascade(label = "Herramientas", menu = archivo_herramientas_menu)
barramenu.add_cascade(label = "Ayuda", menu = archivo_ayuda)


root.mainloop()
