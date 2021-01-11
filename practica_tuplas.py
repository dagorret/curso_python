miTupla = ("Juan", 12, 1, 1995)

print(miTupla[2])

# Convertir una Tupla en Lista
milista=list(miTupla)
print(milista)
print(miTupla)

miLista = ["Juan", 12, 1, 1995]
# Convertir una Lista en Tupla
miTupla = tuple(miLista)

# Buscar un elemento en una tupla
print("Juan" in miTupla)

# Cuantos elementos se encuentra en una tupla

miTupla = ("Juan", 12, 1, 1995, 12)
print(miTupla.count(12))


# Averiguar la lengitud de una tupla
print(len(miTupla))

# Tuplas unitarias
miTupla = ("Juan",)
print(len(miTupla))

# Tupla sin parentesis
miTupla = "Juan", 12, 1, 1995
print(miTupla)

# Desempaqueta de una tupla
nombre, dia, mes, agno = miTupla
print(nombre)
print(dia)
print(mes)
print(agno)
