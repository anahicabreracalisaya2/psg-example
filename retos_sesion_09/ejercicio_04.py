productos = ["Paleta", "Chicle", "Bon Bon Bum", "Oreo", "Chizitos"]
precios = [2, 5, 1, 4, 3]
print("Las listas son las siguientes:")
print(productos)
print(precios)
# Agregar 2 productos nuevos al final de las listas
productos.extend(["Nucita", "Golpe"])
precios.extend([1, 3])
print("\n Se añadieron productos, ahora la lista es ")
print(productos)
print(precios)

# Eliminar el producto con el nombre "Bon Bon Bum"
print("\n Ahora se elimino Bon Bon Bum:")
val=productos.index("Bon Bon Bum")
productos.pop(val)
precios.pop(val)
print(productos)
print(precios)

# ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
valor1=productos.index("Oreo")
valor2=productos.index("Chizitos")
print("\n Precio de Oreo")
print(precios[valor1])
print("Precio de Chizitos")
print(precios[valor2])

# ¿Cuál es el producto más caro y el más barato?
max_precio = max(precios)
min_precio = min(precios)
producto_mas_caro = productos[precios.index(max_precio)]
producto_mas_barato = productos[precios.index(min_precio)]

print("El producto mas barato es:",producto_mas_barato)
print("El producto mas caro es:", producto_mas_caro)

# ¿Cuántos productos tienes en total?
total_productos = len(productos)
print("\n Se cuenta con:",total_productos, "productos")

# ¿Cuánto cuestan todos los productos?
total_precios = sum(precios)
print("\n Costo de los productos:",total_precios)

# Ordenar los productos y precios del más barato al más caro
i0 = precios.index(min(precios))
p0 = [productos[i0], precios[i0]]

precios1 = precios[:i0] + precios[i0+1:]
productos1 = productos[:i0] + productos[i0+1:]

i1 = precios1.index(min(precios1))
p1 = [productos1[i1], precios1[i1]]

precios2 = precios1[:i1] + precios1[i1+1:]
productos2 = productos1[:i1] + productos1[i1+1:]

i2 = precios2.index(min(precios2))
p2 = [productos2[i2], precios2[i2]]

precios3 = precios2[:i2] + precios2[i2+1:]
productos3 = productos2[:i2] + productos2[i2+1:]

i3 = precios3.index(min(precios3))
p3 = [productos3[i3], precios3[i3]]

precios4 = precios3[:i3] + precios3[i3+1:]
productos4 = productos3[:i3] + productos3[i3+1:]

p4 = [productos4[0], precios4[0]]
pares_ordenados = [p0, p1, p2, p3, p4]

print("Los productos ordenado ssegun el precio son los siguientes: \n",pares_ordenados)


# Eliminar todos los productos y precios
print(total_productos)
precios.clear()
productos.clear()
print("\n Se limpió la lista: ")
print(precios)
print(productos)

