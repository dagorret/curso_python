class Persona():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre:", self.nombre, " Edad:", self.edad, " Residencia: ",
        self.residencia)


class Empleado(Persona):

    def __init__(self, nombre, edad, residencia, salario, antiguedad):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(" Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

antonio = Persona("Antonia", 55, "Argentina")
antonio.descripcion()

jorge = Empleado("Jorge", 43, "Brasil", 1500, 15)
jorge.descripcion()

print(isinstance(jorge, Empleado))
print(isinstance(jorge, Persona))
print(isinstance(antonio, Persona))
print(isinstance(antonio, Empleado))
