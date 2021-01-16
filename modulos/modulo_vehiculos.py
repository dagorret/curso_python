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

class Moto(Vehiculo):
    haciendo_caballito = ""

    def caballito(self):
        self.haciendo_caballito = "Haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\n",
            "Modelo: ", self.modelo, "\n",
            "En Marcha: ", self.en_marcha, "\n",
            "Acelerando: ", self.acelerar, "\n",
            "Frenando: ", self.frenar, "\n",
            self.haciendo_caballito, "\n")

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "LA furgoneta no está cargada"

class VehiculosElectricos(Vehiculo):
    def __init__(self, marca, modelo):
            super().__init__(marca, modelo)
            self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True

class BicicletaElectrica(VehiculosElectricos, Vehiculo):
    pass
