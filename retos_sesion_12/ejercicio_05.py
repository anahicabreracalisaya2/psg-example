
# Entrada de datos
nombre = input("Ingrese el nombre del contacto: ")
numero = input("Ingrese el número de teléfono: ")

# Verificación del número de teléfono
es_numero_valido = (
    len(numero) == 12 and
    numero[0] == "+" and
    numero[1:].isdigit()
)
# Verificación del nombre
if nombre and es_numero_valido:
    contactos = {nombre: numero}
    print("Contacto guardado!")
else:
    print("Datos incorrectos :(")
