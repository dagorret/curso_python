# For con una lista
for i in [1,2,3]:
    print("Hola")

for i in ["primavera", "verano", "otoño", "invierno"]:
        print(i)

for i in ["Píldoras", "Informáticas", 3]:
    print("Hola", end=" ")

for i in "juan@correo.com":
    print(i, end=" ")

print("\n-------\n Prueba de Email simple\n-------\n")
contador = 0
correo = input("Introduce tu email")

for i in correo:
    if i == "@" or i == ".":
        contador = contador + 1

if contador == 2 :
    print("Email Correcto")
else:
    print("Email incorrecto")

print("Range")

for i in range(5):
    print(i)
