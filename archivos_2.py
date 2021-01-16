from io import open

#crear archivo
archivo = open("data.txt", "r")
print(archivo.read())

archivo.seek(0)
print(archivo.read())

archivo.seek(11)
print("==2==")
print(archivo.read())

archivo.seek(0)
print("==3==")
print(archivo.read(10))

archivo.seek(len(archivo.read()) / 2 )
print(archivo.read())
archivo.close()

archivo = open("data.txt", "r")
archivo.seek(len(archivo.readlines()))
print("==4==")
print(archivo.read())
archivo.close()

archivo = open("data.txt", "r+")
archivo.write("Comienzo del texto") ## sobreescribe
archivo.close()

archivo = open("data.txt", "r+")
lista = archivo.readlines()
lista[1] = "Este es un reemplazo \n"
archivo.seek(0)
archivo.writelines(lista)
archivo.close()
