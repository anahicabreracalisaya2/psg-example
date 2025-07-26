## Funcion range
range(5)
range(1,10,2)
range(10, 0, -1)
print(list(range(5)))
## Estructura de un FOR
#for variable in range(inicio, fin, paso):
#print(variable)
### Estructua de control
print ("Inicio")
for i in range(5): # rango (0,5,1)
    print(i)
print ("Fin")
## Ejemplo
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma = suma + i #suma += i
print(suma)
# Ejemplo 1: sumar los números del 1 al 10 de 2 en 2
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma = suma + i #suma += i
print(suma)
##Ejemplo 2: crear un árbol de navidad de 6 niveles

print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")
#Ejemplo 3: crear una serie de números cuadrados del 1 al 10

print ("Ejemplo 3")
for i in range(1, 11):
    print(i**2, end=" ")

#Ejemplo 4: crear una lista de números pares del 1 al 10

print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)
## EJERCICIOS
#Ejercicio 1, imprimir los 10 primeros de la serie números cúbicos
#Solicion
print ("Ejercicio 1")
for i in range(1, 11):
    print(i**3, end=" ")
    
## FOR con secuencias
#for variable in secuencia:
#print(variable)

#Ejemplo 5: imprimir los elementos de una lista fiestas
print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)
#Ejemplo 6: imprimir los elementos de una tupla de frutas separados por coma

print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")

#Ejemplo 7: imprimir los elementos de un diccionario

print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])

#Ejemplo 8: imprimir los elementos del ciclo de vida de un pollo con flechas

print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")

## Recorrer elementos con indexacion

#Ejemplo 9: Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)

#Ejemplo 10: Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

print ("Ejemplo 10")
animales = ['🐶','🐱','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])

#Ejemplo 11: Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])

#Ejercicio 2: imprimir la cantidad de veces los elementos de la cadena '⚽🏀🏐🎱' de acuerdo a su posición más 1
print ("Ejercicio 2")
esferas = '⚽🏀🏐🎱'
for i, esfera in enumerate(esferas):
    print(esfera*(i+1))

## Estructura de un WHILE
#while condicion:
#print("Código a ejecutar")

#Ejemplo 12: imprimir los números mientras sean menores o igual a 5 empezando desde 0

print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1

#Ejemplo 12: imprimir los números mientras sean menores o igual a 5 empezando desde 0

print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1
#Ejemplo 13 sumar los números mientras no se ingrese por teclado el número 0

print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)

#Ejercicio 3, Ingresa un número por teclado y genera un contador hasta 0, si el número es negativo no hace nada
print ("Ejercicio 3")
numero = int(input("Ingrese un número: "))
while numero >= 0:
    print(numero)
    numero -= 1
## BREAK
#Ejemplo 14, De la siguiente lista de frutas imprimir los elementos hasta que se encuentre un gusano 🐛 con for

frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")
#Con un WHILE
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")
#Ejemplo 15, Crear un ciclo infinito que imprima un contador incremental

print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1

#Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto la ponga en mayúsculas y la imprima hasta que se ingrese la palabra salir

print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")

#Ejercicio 4, Crear un ciclo infinito que reciba un número por teclado y verifique si es par o impar hasta que se ingrese el número 0
print ("Ejercicio 4")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print ("Par" if numero % 2 == 0 else "Impar")

#Estructura de una lista por comprensión
#[expresion for variable in secuencia]

#Estructura de una lista por comprensión y condicional
#[expresion for variable in secuencia if condicion]

#Ejemplo 17, Crear una lista de los números pares del 2 al 10
print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)
#Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional

print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)

#Ejemplo 19, Crear un diccionario números 2 al 10 donde si es par vale "Par" y si es impar valga "Impar"
print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)

#Ejercicio 5, Crear una tupla de los números impares del 1 al 10 usando una tupla por comprensión
print ("Ejercicio 5")
impares = tuple(i for i in range(1, 11) if i % 2 != 0)
print(impares)

## Ciclos anidados
#Ejemplo 20, Imprimir las tablas de multiplicar del 1 y 2

print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
#Ejemplo 21, Introducir un número por teclado y crear una tabla de multiplicar de ese número del 1 al 10, si se ingresa 0 termina el programa

print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")

##Matrices
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
#Ejemplo 22, Introducir un número por teclado y crear una matriz nxn con la letra X
print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
#Ejercicio 6, Crear una matriz ingresando un número por teclado para el tamaño de la matriz y en cada posición colocar una tupla con (i, j)
print ("Ejercicio 6")
n = int(input("Ingrese un número: "))
matriz = [[(j, i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)


