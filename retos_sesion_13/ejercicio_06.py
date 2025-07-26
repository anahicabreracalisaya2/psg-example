while True:
    numero = int(input("Escribe una numero o '0' para terminar): "))
    
    if numero == 0:
        break
    if numero % 7 ==0:
        print("Es divisible entre 7")
    else:
        print("No es divisible entre 7")