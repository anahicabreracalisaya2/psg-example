def promedio(calificaciones):
    total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = total / cantidad
    return promedio

# datos y llamada de la función
calificaciones = [50, 75, 80, 91, 70]
promedio = promedio(calificaciones)
print("El promedio de las calificaciones es:", promedio)
 