def generaPares(limite):
    num = 1
    miLista = []

    while num < limite:
        miLista.append(num * 2)
        num += 1
    
    return miLista


print(generaPares(1000000))


def generatorPares(limite):
    num = 1

    while num < limite:
        yield num * 2
        num += 1

devuelvePares = generatorPares(10)

for i in devuelvePares:
    print(i)

# Solo buscar ciertos elementos

devuelvePares = generatorPares(10)
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))

#devuelvePares = generatorPares(1000000)
#for i in devuelvePares:
#    print(i, end="")
