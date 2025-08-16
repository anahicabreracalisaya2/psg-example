while True:
    frase = input("Escribe una frase o 'salir' para terminar: ").lower()
    
    if "salir" in frase :
        break
    aux = ""
    for i in range(len(frase) - 1, -1,-1):
        aux += frase[i]
    if aux == frase:
        print("Es palíndromo")
    else:
        print("No es palíndromo")