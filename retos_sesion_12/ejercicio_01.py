#Crear un script que pida un número entero y verifique si es múltiplo de 5 usando operador ternario.
numero = int(input("Número entero: "))
resultado="Es multiplo de 5" if numero % 5 == 0 else "No es multiplo de 5"
print(resultado)