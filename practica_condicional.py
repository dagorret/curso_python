edad = 8

# Condiciones encadenadas
if 0 < edad < 100:
    print("Edad Correcta")
else:
    print("Edad Incorrecta")

salario_presidente = int(input("Introduce salario presidente "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce salario jefe de área "))
print("Salario jefe área: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario administrativo "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")
