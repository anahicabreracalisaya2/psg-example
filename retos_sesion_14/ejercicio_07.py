# Tablero vacío
tablero = [[" " for i in range(3)] for j in range(3)]

# Jugador inicial
jugador_actual = "X"

# Mostrar el tablero
def mostrar_tablero():
    print("  1 2 3")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()

# Verificar si hay ganador
def hay_ganador():
    for i in range(3):
        # Filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        # Columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False

# Verificar si hay empate
def es_empate():
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

# Función principal del juego
def jugar():
    global jugador_actual

    while True:
        mostrar_tablero()
        print("Turno del jugador:", jugador_actual)

        # Validación con while
        while True:
            fila = int(input("Ingresa la fila (1, 2, 3): ")) - 1
            columna = int(input("Ingresa la columna (1, 2, 3): ")) - 1

            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Fila o columna fuera de rango, intenta de nuevo.")
            elif tablero[fila][columna] != " ":
                print("Esa casilla ya está ocupada, intenta de nuevo.")
            else:
                break  # Entrada válida

        # Colocar la ficha
        tablero[fila][columna] = jugador_actual

        # Verificar si ganó
        if hay_ganador():
            mostrar_tablero()
            print("Ganó el jugador:", jugador_actual )
            break

        # Verificar si es empate
        if es_empate():
            mostrar_tablero()
            print("Es un empate :(")
            break

        # Cambiar de jugador
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"

# Ejecutar el juego
jugar()