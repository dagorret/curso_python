class Coche():

    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4 ##protección de la propiedad
        self.__en_marcha = False

    def arrancar(self, arracamos):
        self.__en_marcha = arracamos
        if self.__en_marcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El cocche tiene ", self.__ruedas, " ruedas.",
                "Un ancho de ", self.__ancho_chasis,
                " y un largo de ", self.__largo_chasis)


mi_coche = Coche()

print(mi_coche.arrancar(True))
mi_coche.estado()

print("-----------Segundo objecto--------------")

mi_coche_2 = Coche()
print(mi_coche_2.arrancar(False))
mi_coche_2.__ruedas = 5
mi_coche_2.estado()
