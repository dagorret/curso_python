from tkinter import *
from tkinter import filedialog

root = Tk()

def abre_fichero():
    tipos=(("Fichero Texto", "*.txt"), ("Python", "*.py"), ("Todos", "*.*") )
    fichero = filedialog.askopenfilename(title="Abrir", initialdir=".", filetypes = tipos)
    print(fichero)

Button(root, text="Abrir Fichero", command=abre_fichero).pack()

root.mainloop()
