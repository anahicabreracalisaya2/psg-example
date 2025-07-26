while True:
    original = input("Escribe una frase o 'salir' para terminar): ")
    frase=original.lower
    if frase == "salir":
        break
    aux = ""
    for i in range(len(frase) - 1, -1, -1):
        aux += frase[i]
    if aux == frase:
        print("Es palíndromo")
    else:
        print("No es palíndromo")