# Entrada de datos
numero1=int(input("Ingrese el primer valor: "))
numero2=int(input("Ingrese el segundo valor: "))
ope=input("Ingrese la operación: ")
resultado="invalido"
# Calculadora
if ope == "+" or ope == "-" or ope == "*" or ope == "/" :
    if ope == "+":
        resultado = numero1 + numero2
    elif ope == "-":
        resultado = numero1 - numero2
    elif ope == "*":
        resultado = numero1 * numero2
    elif ope == "/" and numero2 != 0:
        resultado = numero1 / numero2
    print("El resultado es:" ,resultado)
else:
    print("Operación inválida")