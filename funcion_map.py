class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de $ {}".format(self.nombre, self.cargo, self.salario)


listaEmpleado = [
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "Presidente", 7500),
    Empleado("Antonio", "Administrativo", 2100),
    Empleado("Mario", "Botones", 1800),
]

def calculo_comision(empleado):
    if empleado.salario <= 3000:
        empleado.salario = empleado.salario * 1.03

    return empleado

lista_empleados_comision = map(calculo_comision, listaEmpleado)

for e in lista_empleados_comision:
    print(e)
