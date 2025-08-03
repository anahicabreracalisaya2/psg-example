def contador(lista):
    impares=[val for val in lista if val%2==0]
    pares=[val for val in lista if val%2!=0]
    return pares, impares
lista=[1,2,3,4,5,6,7,8,9,10]
par,impar=contador(lista)
print("Los pares son:",par)
print("Los impares son:",impar)