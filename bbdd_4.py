import sqlite3

mi_conexion = sqlite3.connect("base_3_3.db")

cursor = mi_conexion.cursor()


# cursor.execute('''
#     CREATE TABLE productos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre VARCHAR(50) UNIQUE,
#     precio INTEGER,
#     seccion VARCHAR(20))
#     ''')
#
# productos = [
#     ("pelota", 20, "jugetería"),
#     ("pantalón", 15, "vestimenta"),
#     ("destonillador", 25, "ferretería"),
#     ("jarrón", 45, "cerámica")
# ]
# cursor.executemany("INSERT INTO productos VALUES(NULL,?,?,?)", productos)

cursor.execute("UPDATE productos SET precio=35 WHERE nombre='pelota'")
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

cursor.execute("DELETE FROM productos WHERE id=4")
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

mi_conexion.commit()
mi_conexion.close()
