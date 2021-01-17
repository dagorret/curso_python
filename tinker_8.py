from tkinter import *

root = Tk()

barramenu = Menu(root)
root.config(menu=barramenu, width = 300, height=300)

archivo_menu = Menu(barramenu, tearoff=0)
archivo_menu.add_command(label = "Nuevo")
archivo_menu.add_command(label = "Guardar")
archivo_menu.add_command(label = "Guardar como")
archivo_menu.add_separator()
archivo_menu.add_command(label = "Cerrar")
archivo_menu.add_command(label = "Salir")

archivo_edicion_menu = Menu(barramenu, tearoff = 0)
archivo_edicion_menu.add_command(label = "Copiar")
archivo_edicion_menu.add_command(label = "Cortar")
archivo_edicion_menu.add_command(label = "Pegar")
archivo_herramientas_menu = Menu(barramenu)
archivo_ayuda = Menu(barramenu, tearoff = 0)
archivo_ayuda.add_command(label = "Licencia")
archivo_ayuda.add_command(label = "Acerca de ..")

barramenu.add_cascade(label = "Archivo", menu = archivo_menu)
barramenu.add_cascade(label = "Edición", menu = archivo_edicion_menu)
barramenu.add_cascade(label = "Herramientas", menu = archivo_herramientas_menu)
barramenu.add_cascade(label = "Ayuda", menu = archivo_ayuda)


root.mainloop()
