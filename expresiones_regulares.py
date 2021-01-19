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

lista_nombres = ["Ana Gomez",
                "Maria Martin",
                "Sandra Lopez",
                "Santiago Martin",
                "Sandra Fernandez"]

for e in lista_nombres:
    if re.findall('^Sandra', e):
        print(e)

for e in lista_nombres:
    if re.findall('Martin$', e):
        print(e)

lista_dominios = ["http://pildorasinformaticas.es",
                  "ftp://pildorasinformaticas.es",
                  "http://pildorasinformaticas.com",
                  "ftp://pildorasinformaticas.com",
                  "http://informaticaespaña.com"
                 ]
for e in lista_dominios:
    if re.findall("^ftp", e):
        print(e)

for e in lista_dominios:
    if re.findall("[ñ]", e):
        print(e)



lista_nombres_2 = [
"Ana",
"Pedro",
"María",
"Rosa",
"Sandra",
"Celia"
]

for e in lista_nombres_2:
    if re.findall('[o-t]$', e):
        print(e)
