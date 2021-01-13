def evaluarEdad(edad):
    if edad < 0:
        raise TypeError("Las edades negativas son incorrectas")
    if edad < 20:
        return "eres muy jove"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "cuidate ..."


print(evaluarEdad(70))

import math

def calculaRaiz(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num)

op1 = int(input("Introduce un número"))

try:
    print(calculaRaiz(op1))
except ValueError as ErrordeNumeroNegativo:
    print(ErrordeNumeroNegativo)

print("Programa Terminado")
