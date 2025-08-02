def serie_de_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return serie_de_lucas(n - 1) + serie_de_lucas(n - 2)

aux=serie_de_lucas(4)
print("La posición 5 es:", aux)