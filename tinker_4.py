from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

minombre = StringVar()
CuadroTexto = Entry(miFrame, textvariable=minombre)
CuadroTexto.grid(row=0, column=1, padx=10, pady=10)
vLabel = Label(miFrame, text="Nombre:")
vLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

CuadroApellido = Entry(miFrame)
CuadroApellido.grid(row=1, column=1, padx=10, pady=10)
vLabel2 = Label(miFrame, text="Apellido:")
vLabel2.grid(row=1, column=0, sticky="e", padx=10, pady=10)

CuadroDireccion = Entry(miFrame)
CuadroDireccion.grid(row=2, column=1, padx=10, pady=10)
vLabel3 = Label(miFrame, text="Dirección de Casa:")
vLabel3.grid(row=2, column=0, sticky="e", padx=10, pady=10)

CuadroPassword = Entry(miFrame)
CuadroPassword.grid(row=3, column=1, padx=10, pady=10)
CuadroPassword.config(show="*")
vLabel4 = Label(miFrame, text="Password:")
vLabel4.grid(row=3, column=0, sticky="e", padx=10, pady=10)

CuadroComentario = Text(miFrame, width=16, height=5)
CuadroComentario.grid(row=4, column=1, padx=10, pady=10)
vLabel5 = Label(miFrame, text="Comentario:")
vLabel5.grid(row=4, column=0, sticky="e", padx=10, pady=10)
scrollbar = Scrollbar(miFrame, command=CuadroComentario.yview)
scrollbar.grid(row=4, column=2, sticky="nsew")
CuadroComentario.config(yscrollcommand=scrollbar.set)

def codigoBoton():
    minombre.set("Carlos")
    
EnviarButton = Button(root, text="Enviar", command=codigoBoton)
EnviarButton.pack()

root.mainloop()
