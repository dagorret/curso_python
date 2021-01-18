'''def area_triangulo(base, altura):
    return base*altura/2

print(area_triangulo(5,7))

t1 = area_triangulo(5,7)
t2 = area_triangulo(9,6)

print(t1)
print(t2) '''

area_triangulo = lambda base, altura: base*altura/2

print(area_triangulo(7,5))
print(area_triangulo(9,6))

cubo = lambda n: pow(n,3)

print(cubo(13))


destacar = lambda t: "¡${}".format(t)

comision = 15585

print(destacar(comision))
