estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for estudiante in estudiantes:
    nombre, nota = estudiante
    if nota >= 51:
        print("Muchas felicidades", nombre, "Aprobaste con",nota,"puntos.")
