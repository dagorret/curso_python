import sqlite3

mi_conexion = sqlite3.connect("base3.db")

cursor = mi_conexion.cursor()
#cursor.execute("CREATE TABLE producto (nombre_articulo VARCHAR(50), precio INTERGER, seccion VARCHAR(20))")

cursor.execute("INSERT INTO producto VALUES('Balón', 15, 'Deportes')")
mi_conexion.commit()

mi_conexion.close()
