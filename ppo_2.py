class Coche():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False

    def arrancar(self, arracamos):
        self.en_marcha = arracamos
        if self.en_marcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El cocche tiene ", self.ruedas, " ruedas.",
                "Un ancho de ", self.ancho_chasis,
                " y un largo de ", self.largo_chasis)


mi_coche = Coche()

print(mi_coche.arrancar(True))
mi_coche.estado()

print("-----------Segundo objecto--------------")

mi_coche_2 = Coche()
print(mi_coche_2.arrancar(False))
mi_coche_2.estado()
