from tkinter import *

root = Tk()
root.title("Ejemplo")

foto = PhotoImage(file = "avion.png")

Label(root, image = foto).pack()

frame = Frame(root)
frame.pack()

playa = IntVar()
montagna = IntVar()
rural = IntVar()

def opciones():
    opcion_escogida = ""

    if playa.get() == 1:
        opcion_escogida += " playa"

    if montagna.get() == 1:
        opcion_escogida += " montaña"

    if rural.get() == 1:
        opcion_escogida += " rural"

    texto_final.config(text = opcion_escogida)

Label(frame, text = "Elege destinos", width = 50).pack()
Checkbutton(root, text="Playa", variable = playa, onvalue = 1, offvalue=0, command = opciones).pack()
Checkbutton(root, text="Montaña", variable = montagna, onvalue = 1, offvalue=0, command = opciones).pack()
Checkbutton(root, text="Rural", variable = rural, onvalue = 1, offvalue=0, command = opciones).pack()

texto_final = Label(root)
texto_final.pack()

root.mainloop()
