# Entrada de datos
entrada=input("Ingrese dos valores y el operador separados por comas: ")
a1=entrada.find(",")
a2=entrada.find(",",a1+1)
numero1 = float(entrada[:a1])
numero2 = float(entrada[a1+1:a2])
ope = entrada[a2+1]
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