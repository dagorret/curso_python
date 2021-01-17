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

    def __init__(self):
        archivo = open("personas.dat", "ab+")
        archivo.seek(0)

        try:
            self.personas = pickle.load(archivo)
            print("Se cargaron {} personas".format(len(personas)))
        except:
            print("El fichero está vació")
        finally:
            archivo.close()
            del(archivo)

    def agregar(self, p):
        self.personas.append(p)
        self.guardar()

    def mostrar(self):
        for p in self.personas:
            print(p)

    def guardar(self):
        archivo = open("personas.dat", "wb")
        pickle.dump(self.personas, archivo)
        print("aca")
        archivo.flush()
        archivo.close()
        del(archivo)

    def info(self):
        print("La info del fichero es")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()
p = Persona("Sandra", "Femenino", 29)
miLista.agregar(p)
p = Persona("Antonio", "Masculini", 33)
miLista.agregar(p)
p = Persona("Ana", "Femenino", 18)
miLista.agregar(p)

miLista.mostrar()

print("Fichero")
miLista.info()
