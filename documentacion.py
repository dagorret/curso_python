from modulos import funciones_matematicas

class Areas:
    """Esta clase calcula las áreas de diferentes figura geométricas"""
    def area_cuadrado(lado):
        """ Calcula el área de un area_cuadrado
        elevevando al cuadrado el lado pasad por parámetro"""

        return "El área de un cuadrado es: " + str(lado * lado)

    def area_triangulo(base, altura):
        """ Calcula el área de un triangulo utilizando los parámetros base y altura"""
        return "El área de un triangulo es: " + str(base * altura/2)


help(funciones_matematicas)
