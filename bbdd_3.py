import sqlite3

mi_conexion = sqlite3.connect("base_2_3.db")

cursor = mi_conexion.cursor()
#cursor.execute("CREATE TABLE producto (nombre_articulo VARCHAR(50), precio INTERGER, seccion VARCHAR(20))")

# cursor.execute('''
#     CREATE TABLE productos (
#     codigo VARCHAR(4) PRIMARY KEY,
#     nombre VARCHAR(50),
#     precio INTEGER,
#     seccion VARCHAR(20))
#     ''')
#
# productos = [
#     ("AR01", "pelota", 20, "jugetería"),
#     ("AR02", "pantalón", 15, "vestimenta"),
#     ("AR03", "destonillador", 25, "ferretería"),
#     ("AR04", "jarrón", 45, "cerámica")
# ]
# cursor.executemany("INSERT INTO productos VALUES(?,?,?,?)", productos)

#cursor.execute("INSERT INTO productos VALUES('AR05','tren',15,'juegetería')")

cursor.execute('''
    CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50),
    precio INTEGER,
    sccion VARCHAR(20))
    ''')

productos = [
    ("pelota", 20, "jugetería"),
    ("pantalón", 15, "vestimenta"),
    ("destonillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica")
]
cursor.executemany("INSERT INTO productos VALUES(NULL,?,?,?)", productos)

mi_conexion.commit()
mi_conexion.close()
