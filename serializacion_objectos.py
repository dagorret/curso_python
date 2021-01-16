import pickle

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.en_marcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print("Marca:", self.marca, "\n",
            "Modelo: ", self.modelo, "\n",
            "En Marcha: ", self.en_marcha, "\n",
            "Acelerando: ", self.acelerar, "\n",
            "Frenando: ", self.frenar, "\n")


coche1 = Vehiculo("Ford", "MKS")
coche2 = Vehiculo("Fiat", "Chronos")
coche3 = Vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("coches.dat", "wb")
pickle.dump(coches, fichero)
fichero.close()

fichero = open("coches.dat", "rb")
lista_coches = pickle.load(fichero)
fichero.close()

for c in lista_coches:
    print(c.estado())
