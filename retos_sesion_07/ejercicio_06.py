# Funciones no vistas
# Verificar minusculas
ver='america'.islower()
print(ver, type(ver))

#aumentar valores ceros a un numero
aux="42".zfill(5)
print(aux)

#remover palabras
palabra="departamento en venta".removesuffix("n venta")
print(palabra)

# alinear en un rango especifico
texto = "Hola"
resultado = texto.rjust(10)
print(resultado) 

# comparar sin importar minusculas o mayusculas
texto1 = "Café"
texto2 = "café"  
print(texto1.casefold() == texto2.casefold()) 

#Texto imprimible
texto3 = "Hola Mundo!"
print(texto3.isprintable())  
texto4 = "Hola\nMundo"
print(texto4.isprintable())  