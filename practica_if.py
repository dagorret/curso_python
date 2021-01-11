def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5 :
        valoracion = "suspenso"
    return valoracion

print("Progama de evaluación de notas de alumnos:")
nota_alumno = int(input("Introduce la nota del alumno"))
print(evaluacion(nota_alumno))
