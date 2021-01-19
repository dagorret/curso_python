def area_triangulo(base, altura):
    """
    Calcula el area de un area_triangulo

    >>> area_triangulo(3,6)
    'El area es: 9.0'
    """
    return "El area es: " + str(base * altura / 2)


print(area_triangulo(2,4))


import doctest
doctest.testmod()
