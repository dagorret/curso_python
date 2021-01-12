for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)

nombre = "Pildoras Informáticas"
contador = 0

for letra in nombre:
    if letra == " ":
        continue
    contador += 1

print(contador)

# Pass
class MiClase:
    pass

def MiFuncion():
    pass #implementar mas tarde

email = input("Email: ")
for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)
