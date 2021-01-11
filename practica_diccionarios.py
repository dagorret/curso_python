miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario["Francia"])

print(miDiccionario)

# Agregar elementos
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

# Modificar un valor
miDiccionario["Italia"] = "Roma"
print(miDiccionario)


# Eliminar Elementos
del miDiccionario["Reino Unido"]
print(miDiccionario)

# Diccionarios de tipos diferentes
miDiccionario = {"Alemania": "Berlin", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario)

# Diccionario y tuplas como indices
miTupla = ("España", "Francia", "Reino Unido", "Alemania")
miDiccionario = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}
print(miDiccionario)
print(miDiccionario["Francia"])

miDiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993, 1996,1997,1998]}}
print(miDiccionario)

# las claves de un diccionario
print(miDiccionario.keys())
print(miDiccionario.values())

# Longitus del diccionario
print(len(miDiccionario))
