
tablero=[["#" for i in range(8) ] for j in range(8)]

for i in range(8):
    for j in range(8):
        if (j+i)%2 != 0:
            tablero[i][j]="*"
for i in range(8):
    for j in range(8):
        print(tablero[i][j], end=" ")
    print()