a = 2
b = 1
contador = 0
print("Susesion de Lucas")
while contador < 20:
    print(a)
    regla = a + b
    a = b
    b = regla
    contador =contador+ 1
