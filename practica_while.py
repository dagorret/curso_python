import math

# While determinado
i = 1

while i <= 10:
    print(i)
    i = i + 1

# While indeterminado
edad = int(input("Introduce la edad"))

while edad < 5 or edad > 100 :
    print("Has introducido una edad incorrecta. Vuelve a intentarlo.")
    edad = int(input("Introduce la edad"))

print(f"La edad introducidad es {edad}")

# salir de un blucle
print("Programa de cálculo de raiz cuadrado")
numero = int(input("Introduce un número"))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")
    if intentos == 2:
        print("Demasiados intentos. Finaliza programa")
        break

    numero = int(input("Introduce un número"))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")

