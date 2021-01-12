#Formatos tipo F de string
for i in range(5):
    print(f"Valor de la variable {i}")

# range desde hasta
for i in range(5,10):
    print(f"Valor: {i}")

#range desde hasta en incrementos datos
for i in range(5,50, 3):
    print(f"Valor: {i}")

# Utilizar la función len
valido = False
email = input("Email:")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

