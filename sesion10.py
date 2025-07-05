##Tipos de conjuntos
print ("Conjunto de enteros")
conjunto = {1, 2, 3, 4, 5}
print(conjunto) 
print(type(conjunto))
print ("Conjunto de cadenas")
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto)
print(type(conjunto))
print ("Conjunto mixto")
conjunto = {1, True, 3.14, '☕'}
print(conjunto)
print(type(conjunto))
print ("Conjunto vacío")
conjunto = set()
print(conjunto)
print(type(conjunto))
print ("Conjunto a partir de la cadena")
cadena = 'Hola Mundo'
conjunto = set(cadena)
print(conjunto)
print(type(conjunto))
print ("Conjunto a partir de una tupla")
tupla = (1, 2, 3, 4, 5, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))
print ("Conjunto a partir de una lista")
lista = [True, False, 0, 1]
conjunto = set(lista)
print(conjunto)
print(type(conjunto))
print ("Conjunto por comprensión")
conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
print(conjunto)
print(type(conjunto))
## Comando "SET"
## No funciona como los demas, por sus caractersticas

conjunto = {1, 2, 3, 4, 5}
#print(conjunto[0]) 
conjunto = {1, 2, 3, 4, 5}
#print(conjunto[0:3]) # TypeE
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
print(conjunto1 + conjunto2)
conjunto = {1, 2, 3}
print(conjunto * 3)

## Metodos de los conjuntos
print ("Método add()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.add('🥗')
print(conjunto) 
print ("Método update()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.update(['🥤','🍦'])
print(conjunto) 
conjunto.update('🍩🍪')
print(conjunto) 
conjunto.update(('🍫','🍬'))
print(conjunto)
conjunto.update({'🍭','🍮'})
print(conjunto)

## Metodos de eliminación
print ("Método remove()")
conjunto = {'🍕','🍔','🍟','🌭'} 
print (conjunto)
conjunto.remove('🍔')
print(conjunto)
print ("Método discard()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.discard('🍔')
print(conjunto)
conjunto.discard('🍔')
print(conjunto)
print ("Método pop()")
conjunto = {'🍕','🍔','🍟','🌭', '🥤','🍦'}
print (conjunto)
print(conjunto.pop())
print(conjunto)
print(conjunto.pop())
print(conjunto)
print ("Método clear()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.clear()
print(conjunto)
## Operaciones con conjuntos
print ("Método union()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1.union(conjunto2)
print(union)
print ("Método intersection()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
print ("Método difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1.difference(conjunto2)
print("1 y 2:",diferencia)
diferencia = conjunto2.difference(conjunto1)
print("2 y 1:",diferencia)
print ("Método symmetric_difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)

## Metodos de asignación
print ("Método intersection_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.intersection_update(conjunto2)
print(conjunto1)
print ("Método difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1.difference_update(conjunto2)
print ("1:",conjunto1, "2:",conjunto2)
print ("Método difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1.difference_update(conjunto2)
print ("1:",conjunto1, "2:",conjunto2)
print ("Método symmetric_difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

## Metodos de busqueda
print ("Método issubset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es subconjunto del conjunto2?
print(conjunto1.issubset(conjunto2))
# ¿El conjunto3 es subconjunto del conjunto1?
print(conjunto3.issubset(conjunto1))
print ("Método issuperset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto2)) 
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto3)) 
print ("Método isdisjoint()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 no tiene elementos en común con el conjunto2?
print(conjunto1.isdisjoint(conjunto2))
# ¿El conjunto1 no tiene elementos en común con el conjunto3?
print(conjunto1.isdisjoint(conjunto3))

##Metodo de copia
print ("Asignación por referencia")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto
copia.add('🥗')
print(conjunto)
print(copia)
print ("Método copy()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto.copy()
copia.add('🥗')
print(conjunto)
print(copia)

## Funciones de conjuntos
print ("Función len()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(len(conjunto))
print ("Función max()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (max(conjunto))
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(max(conjunto))
print ("Función min()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (min(conjunto))
conjunto = {'🍨','🍔','🍟','🍕'}
print (conjunto)
print(min(conjunto))
print ("Función sum()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (sum(conjunto))

## Operadores con conjuntos
print ("Operador |=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)
print ("Operador ==")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 == conjunto2)
print(conjunto1 == conjunto3)
print ("Operador ==")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 == conjunto2)
print(conjunto1 == conjunto3)
print ("Operador <")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 < conjunto2)
print(conjunto1 < conjunto3)
print ("Operador >")
conjunto1 = {'🍔','🍟','🥤','🍕'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 > conjunto2)
print(conjunto1 > conjunto3)
print ("Operador <=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 <= conjunto2)
print(conjunto1 <= conjunto3)
print ("Operador >=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 >= conjunto2)
print(conjunto1 >= conjunto3)
## Operadores para operaciones con conjuntos
print ("Operador |")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1 | conjunto2
print(union)
print ("Operador &")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1 & conjunto2
print(interseccion)
print ("Operador -")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1 - conjunto2
print("1 - 2:",diferencia)
diferencia = conjunto2 - conjunto1
print("2 - 1:",diferencia)
print ("Operador ^")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)

## Operadores para asignación con operaciones
print ("Operador |= Unión")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)
print ("Operador &= Intersección")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 &= conjunto2
print(conjunto1)
print ("Operador -= Diferencia")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1 -= conjunto2
print("1 - 2:",conjunto1)
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 -= conjunto1
print("2 - 1:",conjunto2)
print ("Operador ^= Diferencia simétrica")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 ^= conjunto2
print(conjunto1)

## Conjuntos inmutables
conjunto = frozenset({'🍔','🍕','🥗','🍟','🌭'})
print(conjunto)
print(type(conjunto))
conjunto = frozenset({1, 2, 3, 4, 5})
print(conjunto)
#Nos sale erorres en operaciones comunes
#print(conjunto.add(6)) # AttributeError: 'frozenset' object has no attribute 'add'
#print(conjunto.remove(1)) # AttributeError: 'frozenset' object has no attribute 'remove'
#print(conjunto |= {6}) 

## Conjuntos anidados
print ("Conjunto de conjuntos")
conjunto = {frozenset({'🍅','🍓','🍎'}), frozenset({'🍈','🍐','🍏'})}
print(conjunto)
print(type(conjunto))
print ("Conjunto de conjuntos")
conjunto = {{'🍅','🍓','🍎'}, {'🍈','🍐','🍏'}} #TypeError: unhashable type: 'set'
print(conjunto)
print(type(conjunto))
