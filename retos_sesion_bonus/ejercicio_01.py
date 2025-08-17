frutas = ['🍅','🍇','🍈','🍉','🍊','🍌','🍍','🍌','🍊','🍉','🍈','🍇','🍅','🍅','🍇']

# Función para contar las frutas
def contar_frutas(lista_frutas):
    contador = {}
    for fruta in lista_frutas:
        if fruta in contador:
            contador[fruta] += 1
        else:
            contador[fruta] = 1
    return contador

# Función para imprimir el conteo de frutas
def imprimir_conteo(conteo):
    for fruta in conteo:
        cant=conteo[fruta]
        sufi= "s." if cant>1 else "."
        print(f"Hay {conteo[fruta]} {fruta} {sufi}")

# Llamando a las funciones
conteo_frutas = contar_frutas(frutas)
imprimir_conteo(conteo_frutas)