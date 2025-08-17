def obtener_aleatorio():
    numeros = list(range(1, 101))
    i=((numeros[0]*17+numeros[-1])%len(numeros))
    secreto = numeros.pop(i)
    return secreto

def adivina(secreto):
        intentos = 0
        print ("Que número estoy pensando? (1-100)")
        while True:
            try:
                intento = int(input(f"Intento N°: {intentos+1}: "))
                if intento == secreto:
                    print ("Felicidades! Has adivinado el número!")
                    break
                elif intento < secreto:
                    print ("El número es mayor.")
                else:
                    print ("El número es menor.")
            except ValueError:
                print ("Por favor, ingresa un número válido.")
            finally:
                intentos += 1
        print (f"Has adivinado el número en {intentos} intentos.\n")

nombre_jugador = "Guest"

def jugar():
    while True:
        print ("Bienvenido al juego de adivinanzas! del Python Study Group 2025")
        print ("="*63)
        nombre_jugador = input("¿Cuál es tu nombre?: ")
        print (f"Bienvenido, {nombre_jugador}!")
        print ("="*63)
        print ()
        opcion = input("Quieres jugar? (s/n): ")
        if opcion.lower() != 's':
            break
        secreto = obtener_aleatorio()
        adivina(secreto)
        print ("="*63)
    print ("Gracias por participar!")
    print (f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()