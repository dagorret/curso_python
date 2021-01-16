import pickle

lista = ["Carlos", "Pedro", "Ana", "Ruben"]

fichero = open("data.dat", "wb")

pickle.dump(lista, fichero)
fichero.close()

del (fichero)

fichero = open("data.dat", "rb")

lista2 = pickle.load(fichero)

print(lista2)
