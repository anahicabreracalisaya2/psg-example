## Estructura de un if
print ("Inicio")
condicion = True
if condicion:
    # Bloque de código
    print ("Cumple condición")
print ("Fin")
# Ejemplo de la estructura: Determinar si es par
print ("Inicio")
numero = 4
if numero % 2 == 0: # Si el módulo de 2 es 0
    print ("El número es par")
print ("Fin")


## Estructura if - else
print ("Inicio")
condicion = False
if condicion:
    # Bloque de código
    print ("Cumple condición")
else:
    # Bloque de código
    print ("No cumple condición")
print ("Fin")
### Ejemplo: Determinar un número impar
print ("Inicio")
numero = 3
if numero % 2 == 0: # Si el módulo de 2 es 0
    print ("El número es par")
else:
    print ("El número es impar")
print ("Fin")

## if anidado 
### Como se declara:
if condicion_1:
    print ("Cumple 1")
    if condicion_2:
        print ("Cumple 2")
    else:
        print ("No cumple 2")
else:
    print ("No cumple 1")
### Estructura:
print ("Inicio Anidado")
condicion_1 = True
condicion_2 = False
if condicion_1:
    print ("Cumple condición 1")
    if condicion_2:
        print ("Cumple condición 2")
    else:
        print ("No cumple condición 2")
else:
    print ("No cumple condición 1")
print ("Fin")

### Ejemplo: Imprimir si un numero es par, impar o cer
print ("Inicio Par, Impar o Cero")
numero = 0  
if numero > 0 or numero < 0:
    if numero % 2 == 0: # Si el módulo de 2 es 0
        print ("El número es par")
    else:
        print ("El número es impar")
else:
    print ("El número es cero")
print ("Fin")

### Declarar un ELIF
if condicion_1:
    print ("Cumple 1")
elif condicion_2:
    print ("Cumple 2")
else:
    print ("No cumple 1 ni 2")

### Estructura de un ELIF
print ("Inicio ELIF")
condicion_1 = False
condicion_2 = True
if condicion_1:
    print ("Cumple condición 1")
elif condicion_2:
    print ("Cumple condición 2")
else:
    print ("No cumple condición 1 ni 2")
print ("Fin")
### Ejemplo: Determinar un valor posititvo, negativo o cero
print ("Inicio Positivo, Negativo o Cero")
numero = -1
if numero > 0:
    print ("El número es positivo")
elif numero < 0:
    print ("El número es negativo")
else:
    print ("El número es cero")

## Operador ternario
### Estructura
print ("Inicio Ternario")
condicion = True
resultado = "Cumple" if condicion else "No cumple"
print (resultado)
print ("Fin")

### Ejemplo: Imprimir si un número es par o impar
print ("Inicio Ternario Par, Impar")
numero = 3
resultado = "El número es par" if numero % 2 == 0 else "El número es impar"
print (resultado)
print ("Fin")

## TRUTHINESS
print ("Truthiness Enteros")
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
print (dividendo,divisor)
if divisor: #divisor != 0
    print (dividendo / divisor)
else:
    print ("No se puede dividir entre cero")
print ("Fin")
# Flotante como condición
print ("Truthiness Flotantes")
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))
print (dividendo,divisor)
if divisor: #divisor != 0.0
    print (dividendo / divisor)
else:
    print ("No se puede dividir entre cero")
print ("Fin")
### Cadena como condición
print ("Truthiness Cadenas")
cadena = input("Cadena: ")
print (cadena)
if cadena: # len(cadena) != 0 or cadena != "" 
    print ("La cadena no está vacía")
else:
    print ("La cadena está vacía")
print ("Fin")
### En tuplas
print ("Truthiness Tuplas")
tupla = tuple(input("Tupla: "))
print (tupla)
if tupla: # len(tupla) != 0 or tupla != ()
    print ("La tupla no está vacía")
else:
    print ("La tupla está vacía")
print ("Fin")
### En listas
print ("Truthiness Listas")
lista = list(input("Lista: "))
print (lista)
if lista: # len(lista) != 0 or lista != []
    print ("La lista no está vacía")
else:
    print ("La lista está vacía")
print ("Fin")
### En conjuntos
print ("Truthiness Conjuntos")
conjunto = set(input("Conjunto: "))
print (conjunto)
if conjunto: # len(conjunto) != 0 or conjunto != set()
    print ("El conjunto no está vacío")
else:
    print ("El conjunto está vacío")
print ("Fin")
### En diccionarios
print ("Truthiness Diccionarios")
diccionario = {}
clave = input("Clave: ")
valor = input("Valor: ")
if clave:
  diccionario = {clave:valor}
print (diccionario)
if diccionario: # diccionario != {}
    print ("El diccionario no está vacío")
else:
    print ("El diccionario está vacío")
print ("Fin")
## NONE
print ("Truthiness None")
valor = None
print (valor, type(valor))
if valor: # valor != None
    print ("El valor no es None")
else:
    print ("El valor es None")
print ("Fin")
### Con operadores ternarios
entero = int(input("Entero: "))
resultado = "Diferente de 0" if entero else "Igual a 0"
print (resultado)
flotante = float(input("Flotante: "))
resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
print (resultado)
cadena = input("Cadena: ")
resultado = "No está vacía" if cadena else "Está vacía"
print (resultado)

### Ejemplo de un dispositico que mode la tempreratura para encender un ventilador
temperatura = float(input("Temperatura: "))
if temperatura > 30:
    print ("Encender ventilador")
elif temperatura < 20:
    print ("Apagar ventilador")
### Ejemplo: Saber si en una cesta estan manzanas y sino comprar
#### Con un if
cesta = ['🍎','🍑','🍓','🍉']
print (cesta)
if '🍎' in cesta:
    print (f"Hay {cesta.count('🍎')} manzanas")
else:
    cesta.extend(['🍎','🍎'])
    print (cesta)
#### Con un operador ternario
cesta = ['🍑','🍓','🍉']
print (cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print (resultado)
print (cesta)


