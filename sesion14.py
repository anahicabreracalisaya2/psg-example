## ESTRUCTURA
def nombre_funcion():
    print ("Bloque de código")
 
nombre_funcion()
### Funciones sin argumentos ni retornos
def funcion():
    print ("Bloque de código")
 
funcion()
### Ejemplo 1, Crear una función para imprimir una lista de 10 números pares y llamarla dos veces
print ("Ejemplo 1")
print ("1. Definir función")
def imprimir_pares():
    pares = [i for i in range(0, 21, 2)]
    print (pares)
 
print ("2. Llamar función")
imprimir_pares()
imprimir_pares()
## Ejercicio 1, crear una función que imprima un mensaje de bienvenida del siguiente conjunto de forma aleatoria
def bienvenida():
    mensajes = {"Bienvenido al Python Study Group 🐍",
    "¡Hola y bienvenido al Python Study Group! ✨",
    "Hola, aprendamos Python juntos 🐍"}
    print (mensajes.pop())

bienvenida()
## FUNCINES SIN ARGUMENTOS Y CON UN RETRONO
def funcion():
    return "Bloque de código"
 
resultado = funcion()
print (resultado)
## Ejemplo 2, Crear una función que devuelva un saludo en diferentes idiomas
print ("Ejemplo 2")
print ("1. Definir función")
def saludo():
    saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
    return saludos.pop()
 
print ("2. Llamar función")
resultado = saludo()
print (resultado)
## Ejercicio 2, Devolver una fruta aleatoria del siguiente conjunto
def devolver_fruta():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    return frutas.pop()

fruta = devolver_fruta()
print (fruta)
## FUNCIONES SIN ARGUMENTOS Y CON MULTIPLE RETORNO
def funcion():
    return "Bloque", "de", "código"

resultado = funcion()
print (resultado)
### 
print ("Ejemplo 3")
print ("1. Definir función")
def saludo():
    saludos_es = {"Hola", "Holi", "Buenos días"}
    saludos_en = {"Hello", "Hi", "Good morning"}
    return saludos_es.pop(), saludos_en.pop()
### Ejemplo 3, Crear una función que devuelva un saludo en dos idiomas
print ("2. Llamar función")
resultado = saludo()
print (resultado)
## Ejercicio 3, Devolver una fruta y un color aleatorio de los siguientes conjunto
def devolver_fruta_color():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    colores = {'🔴','🟠','🟡','🟢','🔵'}
    return frutas.pop(), colores.pop()

fruta, color = devolver_fruta_color()
print (fruta, color)
## FUNCIONES CON UN ARGUMENTO Y SIN RETORNO
def funcion(parametro):
    print (parametro)

funcion("Bloque de código") #1 Argumento
### Ejemplo 4, Crear una función que imprima el cuadrado de un número
print ("Ejemplo 4")
print ("1. Definir función")
def cuadrado(numero):
    print (numero**2)
 
print ("2. Llamar función")
cuadrado(5)
cuadrado(10)
## Ejercicio 4, Crear una función que imprima el mensaje de bienvenida de acuerdo al un idioma enviado como argumento, si no existe imprimir un mensaje por defecto
def bienvenida(idioma):
    mensajes = {
        "es":"Bienvenido al Python Study Group 🐍",
        "en": "Hello and welcome to the Python Study Group! ✨",
    }
    print (mensajes.get(idioma, "¡Hola!"))

bienvenida("es")
bienvenida("en")
bienvenida("fr")
## FUNCIONES CON MÚLTIPLES ARGUMENTOS Y SIN RETORNO
### Estructura
# def funcion(param1, param2, ...,  paramN):
 #   print (param1, param2, ..., paramN)

#funcion("Bloque", "de", "código")
### Ejemplo 5, Crear una función que reciba una cadena y un entero y repita la cadena el número de veces

print ("Ejemplo 5")
print ("1. Definir función")
def repetir(cadena, veces):
    print (cadena*veces)
 
print ("2. Llamar función")
repetir("✨🎉", 10)
## Ejercicio 5, Crear una función que reciba una lista de animales, un entero e imprima una lista con los animales repetidos el número de veces
def repetir_animales(animales, veces):
    lista = [animal*veces for animal in animales]
    print (lista)

animales = ['🐶','🐱','🐭','🐹','🐰']
repetir_animales(animales, 3)

print (resultado)
## FUNCIONES CON MÚLTIPLEAS ARGUMENTOS Y CON UN RETORNO
### Estructura
#def funcion(param1, param2, paramN):
    #return param1

#resultado = funcion("Bloque", "de", "código")
#print (resultado)
## Ejemplo 6, Crear una función que reciba dos números y devuelva una lista con la suma, resta, multiplicación y división de los números

print ("Ejemplo 6")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return [suma, resta, multiplicacion, division]
 
print ("2. Llamar función")
resultado = operaciones(10, 5)
print (resultado)

## Ejercicio 6, Crear una función que reciba dos enteros y una cadena devolver el resultado de la operación de los números según la cadena puede ser suma, resta, multiplicación o división
def operacion(numero1, numero2, operacion):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        return numero1 / numero2
    else:
        return "Operación no válida"

resultado = operacion(10, 5, "suma")
print (resultado)
## FUNCIONES CON MÚLTIPLEAS ARGUMENTOS Y CON MÚLTIPLE RETORNO
### Estructura
#def funcion(param1, param2, ..., paramN):
 #   return param1, param2, ..., paramN

#resultado = funcion("Bloque", "de", "código")
#print (resultado)
### Ejemplo 7, Crear una función que reciba dos números y devuelva la suma, resta, multiplicación y división de los dos números

print ("Ejemplo 7")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division
 
print ("2. Llamar función")
suma, resta, multiplicacion, division = operaciones(10, 5)
print (suma, resta, multiplicacion, division)
## Ejercicio 7, Crear una juego de piedra papel o tijera, donde reciba dos jugadas por teclado y devuelva las jugadas y el resultado, si ingresa salir terminar el juego
def jugar_piedra_papel_tijera(jugada1, jugada2):
    if jugada1 == jugada2:
        resultado = "Empate"
    elif jugada1 == "piedra" and jugada2 == "tijera":
        resultado = "Jugador 1 gana"
    elif jugada1 == "papel" and jugada2 == "piedra":
        resultado = "Jugador 1 gana"
    elif jugada1 == "tijera" and jugada2 == "papel":
        resultado = "Jugador 1 gana"
    else:
        resultado = "Jugador 2 gana"
    return jugada1, jugada2, resultado

while True:
    jugador1 = input("Jugador 1: ")
    if jugador1 == "salir":
        break
    jugador2 = input("Jugador 2: ")
    if jugador2 == "salir":
        break
    resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
    print (resultado)
## VARIABLES GLOBALES Y LOCALES
variable_global = "Variable global"

def funcion():
    variable_local = "Variable local"
    print ("✨",variable_global)
    print ("✨",variable_local)

funcion()
print ("🎈",variable_global)
print ("🎈",variable_local)
## PRIORIDAD
variable = "Variable global"
print ('0.',variable)

def funcion():
    variable = "Variable local"
    print ('1.',variable)

funcion()
print ('2.',variable)
### Ejemplo 8, De la siguiente lista de números obtener el mayor y menor número con una función

numeros = [10, 5, 20, 15, 25, 30] #Global

def mayor_menor(): #No recibe argumentos
    mayor = max(numeros) #Local
    menor = min(numeros) #Local
    return mayor, menor #Devuelve dos valores

resultado = mayor_menor()
print (resultado)
## Ejercicio 8, De la siguiente cadena global convertir en formato título y contar las vocales aeiou con una función
def formato_vocales():
    titulo = cadena.title()
    vocales = sum([1 for letra in titulo if letra in "aeiouAEIOU"])
    return titulo, vocales

cadena = "python es un lenguaje de programación"
resultado = formato_vocales()

print (resultado)
### ARG Y KWARGS
## Estructura
#def funcion(*args):
  #  print (args)
 #   print (type(args))

#funcion("Bloque", "de", "código")
### Ejemplo 9 Crear una función que reciba un número y una cantidad de cadenas, concatene las cadenas y la devuelva repetida N veces
print ("Ejemplo 9")
print ("1. Definir función")
def concatenar(numero, *cadenas):
    concatenado = ""
    for cadena in cadenas:
        concatenado += cadena
    return concatenado*numero
 
print ("2. Llamar función")
resultado = concatenar(3, "🍎", "🍌", "🍍")
print (resultado)
## Ejercicio 9, Crear una función que reciba N objetos y genere una tupla y una lista con los objetos usando *args
def tupla_lista(*args):
    tupla = tuple(args)
    lista = list(args)
    return tupla, lista

lista, tupla = tupla_lista(1, 1.1, True, "🍎")

print (lista)
print (tupla)
## KWARGS
### Estructura
#def funcion(**kwargs):
  #  print (kwargs)
 #   print (type(kwargs))

#funcion(nombre="Jhon", apellido="Doe", genero="M")
### Ejemplo 10, Crear una función que reciba los datos de una persona y devuelva un mensaje con los datos

print ("Ejemplo 10")
print ("1. Definir función")
def datos_persona(**datos):
    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
    return mensaje
print ("2. Llamar función")
resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
print (resultado)
## Ejercicio 10, Crea un simulador de lavar platos con una función que reciba los objetos a lavar y el tiempo de lavado de cada objeto devuelva un mensaje con los objetos lavados y el tiempo total de lavado
def lavar(**objetos):
    tiempo_total = 0
    mensaje = ""
    for objeto, tiempo in objetos.items():
        tiempo_total += tiempo
        mensaje += f"{objeto}: {tiempo} minutos\n"
    mensaje += f"Tiempo total: {tiempo_total} minutos"
    return mensaje

resultado = lavar(plato=5, vaso=3, tenedor=1, cuchara=0.5)
print (resultado)
## DOCUMENTACIÓN DE FUNCIONES
### Estructura
#def funcion():
   # """
    #Documentación aquí
    #"""
    #print ("Bloque de código")
## Acceso a la documentación con .__doc__

print ("Acceso a la documentación")
def funcion():
    """
    Documentación aquí
    """
    print ("Bloque de código")
print (funcion.__doc__)
print ("Fin de la ejecución")
## LLAMADO DE FUNCIONES DENTRO DE FUNCIONES
### Ejemplo 11, Crear tres funciones una principal que reciba un número y dos funciones anidadas que devuelvan el cuadrado y el cubo del número
print ("Ejemplo 11")
print ("1. Definir función Principal")
def principal(numero):
    cuadrado = cuadrado_numero(numero)
    cubo = cubo_numero(numero)
    return cuadrado, cubo
 
print ("2. Definir función Cuadrado")
def cuadrado_numero(numero):
    return numero**2
 
print ("3. Definir función Cubo")
def cubo_numero(numero):
    return numero**3
 
print ("4. Llamar función Principal")
numero = 5
resultado = principal(numero)
print (numero, resultado)
## Ejercicio 11, Crear funciones de limpieza de una cadena para obtener las letras y convertir todo en mayúsculas crea funciones de limpieza y función una principal
ef limpiar_letras(cadena):
    """
    Elimina los números de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayúsculas
    """
    return cadena.upper()

def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)
    return cadena

cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2025"
resultado = limpiar(cadena)
print (cadena)
print (resultado)
## FUNCIONES RECURSIVAS
### Estructura
#def funcion_recursiva(valor):
 #   if caso_base:
  #      return valor
   # else:
    #    return funcion_recursiva(valor)
### Ejemplo 12, Crear una función recursiva para obtener el 10 número par

print ("Ejemplo 12")
print ("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1) + 2
 
print ("2. Llamar función")
resultado = numero_par(10)
print (resultado)
## Ejercicio 12, Crear una función recursiva para obtener el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

resultado = factorial(5)
print (resultado)
## FUNCIONES ANONIMAS O LAMBDA
### Estructura
# lambda argumento: expresión
print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)
## Ejercicio 13, Crear una función anónima para obtener de una cadena las letras solo los alfanuméricos y convertir en mayúsculas
cadena = "Python es un lenguaje de programación"
limpiar = lambda cadena: "".join([letra for letra in cadena if letra.isalnum()]).upper()
resultado = limpiar(cadena)
print (cadena)
print (resultado)
