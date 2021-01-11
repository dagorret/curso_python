miLista = ["María", "Pepe", "Marta", "Antonio"]

# Imprime toda la lista
print(miLista)

#imprime el 3er elemento
print(miLista[2])

#imprime el último elemento por ser negativo. Empieza a contar desde atrás
print(miLista[-1])

#Imprimir a porciiones de la lista
#El primer elemento es inclusivo y el segundo elemento es exclusivo
print(miLista[0:3])

# porciones abreviados
print(miLista[:3])


# acceder desde el elemento 2 hasta el final
print(miLista[2:])

# Añadir elementos a la lista al final
miLista.append("Sandra")
print(miLista)

# Añadir elementos a la lista en una posición especial
miLista.insert(2, "Fabiana")
print(miLista)

# Añadir una lista a lista
miLista.extend(["Pablo", "Juan"])
print(miLista)

# Imprimir el indice de un elemento
print(miLista.index("Antonio"))

# Comprobar si un elemento se encuentra o no en una lista
print("Pepe" in miLista)
print("Sergio" in miLista)


# Lista con distinto tipos de elementos
miLista = ["María", 5, True, 78.35]
miLista.extend(["Sandra", "Ana", "Lucía"])
print(miLista)

# Para eliminar elementos
miLista.remove("Ana")
print(miLista)
miLista.remove(5)
print(miLista)
