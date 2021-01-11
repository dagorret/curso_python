print("Programa de Becas Restrictivo")

distancia_escuela = int(input("Distancia a la escuela"))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos"))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario familiar"))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")



print("Programa de Becas Menos Restrictivo")

distancia_escuela = int(input("Distancia a la escuela"))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos"))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario familiar"))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

