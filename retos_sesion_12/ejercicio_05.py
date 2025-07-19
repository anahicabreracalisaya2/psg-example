
# Entrada de datos
nombre = input("Ingrese el nombre del contacto: ")
numero = input("Ingrese el número de teléfono: ")

# Verificación del número de teléfono
if len(numero) > 11 and numero[0]=="+" and nombre:
    contactos={nombre:numero}
    print("Contacto guardado")
else:
    print("Datos incorrectos")