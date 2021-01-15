class Coche():

    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4 ##protección de la propiedad
        self.__en_marcha = False

    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        if self.__en_marcha:
            chequeo = self.chequeo_interno()

        if self.__en_marcha and chequeo:
            return "El coche está en marcha"
        elif self.__en_marcha and chequeo == False:
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El cocche tiene ", self.__ruedas, " ruedas.",
                "Un ancho de ", self.__ancho_chasis,
                " y un largo de ", self.__largo_chasis)
    
    def chequeo_interno(self):
        print("Realizando Chequeo Interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and 
            self.puertas == "cerradas"):
            return True
        else:
            return False
        

mi_coche = Coche()

print(mi_coche.arrancar(True))
mi_coche.estado()

print("-----------Segundo objecto--------------")

mi_coche_2 = Coche()
print(mi_coche_2.arrancar(False))
mi_coche_2.estado()
