def contar_vocales(cadena):
    vocales = "aeiouAEIOUáéíóú"
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador
aux=contar_vocales("árbol magico")
print("Las vocales en la palabra 'árbol magico' son:",aux)