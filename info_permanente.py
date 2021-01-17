import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se creo un objeto Persona: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas():
    personas = []

    def agregar(self, p):
        self.personas.append(p)

    def mostrar(self):
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
p = Persona("Sandra", "Femenino", 29)
miLista.agregar(p)
p = Persona("Antonio", "Masculini", 33)
miLista.agregar(p)
p = Persona("Ana", "Femenino", 19)
miLista.agregar(p)

miLista.mostrar()
