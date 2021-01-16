from io import open

#crear archivo
archivo = open("data.txt", "w")

frase = "Estupendo día para estudiar Python.\nHoy"

archivo.write(frase)
archivo.close()

archivo = open("data.txt", "r")

texto = archivo.read()
print(texto)
archivo.close()

archivo = open("data.txt", "r")
lineas = archivo.readlines()
archivo.close()
print (lineas)

archivo = open("data.txt", "a")
archivo.write("\n Siempre es una buena ocasión para estudiar")
