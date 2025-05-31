print ("Uso de la Tarjeta y Huella")
tarjeta = True
huella = True
print (tarjeta, "and", huella, "=", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = True
huella = False
print (tarjeta, "and", huella, "=", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = False
huella = True
print (tarjeta, "and", huella, "=", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = False
huella = False
print (tarjeta, "and", huella, "=", (tarjeta or huella) and not (tarjeta and huella))