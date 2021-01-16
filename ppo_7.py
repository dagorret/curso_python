class Coche():

    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")


class Moto():

    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")


class Camion():

        def desplazamiento(self):
            print("Me desplazo con 6 ruedas")


mi_vehiculo = Moto()
mi_vehiculo.desplazamiento()

mi_vehiculo2 = Coche()
mi_vehiculo2.desplazamiento()

mi_vehiculo3 = Camion()
mi_vehiculo3.desplazamiento()

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

print("----------------")
desplazamiento_vehiculo(mi_vehiculo3)
desplazamiento_vehiculo(mi_vehiculo2)
desplazamiento_vehiculo(mi_vehiculo)
