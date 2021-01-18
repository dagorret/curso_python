import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencillo"

texto_buscar = "Python"

print(re.search("aprender", cadena))

if re.search(texto_buscar, cadena) is not None:
    print("Está")
else:
    print("No está")

texto_encontrdo = re.search(texto_buscar, cadena)


print(texto_encontrdo.start())
print(texto_encontrdo.end())
print(texto_encontrdo.span())

print(re.findall(texto_buscar, cadena))
