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
