import sqlite3

mi_conexion = sqlite3.connect("base3.db")

cursor = mi_conexion.cursor()
#cursor.execute("CREATE TABLE producto (nombre_articulo VARCHAR(50), precio INTERGER, seccion VARCHAR(20))")

# cursor.execute("INSERT INTO producto VALUES('Balón', 15, 'Deportes')")

# varios_productos = [
#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerámica"),
#     ("Camión", 20, "Jugetería"),
# ]
#
# cursor.executemany("INSERT INTO producto VALUES (?, ?, ?)", varios_productos)

cursor.execute("SELECT * FROM producto")

varios_productos = cursor.fetchall()

print(varios_productos)

for p in varios_productos:
    print(p)

for p in varios_productos:
    print("Nombre Artículo:", p[0], " Sección:", p[2], " Precio:", p[1])

mi_conexion.commit()



mi_conexion.close()
