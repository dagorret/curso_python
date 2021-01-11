print("Asignaturas optativas")
print("Optativas: Informática gráfica, Pruebas de software, Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida")
asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura no está contemplada")
