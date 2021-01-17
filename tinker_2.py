from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

Label(miFrame, text="Hola Mundo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)
miImagen = PhotoImage(file="icono.png")
Label(miFrame, image=miImagen ).place(x=10, y=10)
root.mainloop()
