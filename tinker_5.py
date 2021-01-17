from tkinter import *

root = Tk()

def imprimir():
    #print("Género: ", opcion.get())
    if opcion.get() == 1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

opcion = IntVar() # Como StrinVar pero en entero

Label(root, text="Género").pack()

Radiobutton(root, text="Masculino", variable=opcion,
            value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=opcion,
            value=2, command=imprimir).pack()
etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
