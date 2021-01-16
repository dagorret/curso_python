cadena = input("Introduce un texto:")

print("Cadena:\n", cadena)

print("Cadena Upper:\n", cadena.upper())
print("Cadena Lower:\n", cadena.lower())
print("Cadena Capitalize:\n", cadena.capitalize())


edad = input("Introduce la edad:\n")
print(edad.isdigit())

while(edad.isdigit() == False):
    print("Introduce un valor numérico")
    edad = input("Introduce la edad:\n")

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")
