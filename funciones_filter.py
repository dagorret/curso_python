def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [16, 24, 39, 51, 92]

print(list(filter(numero_par, numeros)))

print(list(filter(lambda n: n%2==0, numeros)))

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de $ {}".format(self.nombre, self.cargo, self.salario)


listaEmpleado = [
    Empleado("Juan", "Director", 750000),
    Empleado("Ana", "Presidente", 850000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda e: e.salario>50000, listaEmpleado)

for e in salarios_altos:
    print(e)
