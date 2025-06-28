productos = ["Paleta", "Chicle", "Bon Bon Bum", "Oreo", "Chizitos"]
precios = [2, 5, 1, 4, 3]
# Agregar 2 productos nuevos al final de las listas
productos.extend(["Nucita", "Golpe"])
precios.extend([1, 3])
print(productos)
print(precios)

# Eliminar el producto con el nombre "Bon Bon Bum"
val=productos.index("Bon Bon Bum")
productos.pop(val)
precios.pop(val)
print(productos)
print(precios)

# ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
valor1=productos.index("Oreo")
valor2=productos.index("Chizitos")
print(precios[valor1])
print(precios[valor2])

# ¿Cuál es el producto más caro y el más barato?
max_precio = max(precios)
min_precio = min(precios)
producto_mas_caro = productos[precios.index(max_precio)]
producto_mas_barato = productos[precios.index(min_precio)]
print(producto_mas_barato)
print(producto_mas_caro)

# ¿Cuántos productos tienes en total?
total_productos = len(productos)
print(total_productos)

# ¿Cuánto cuestan todos los productos?
total_precios = sum(precios)
print(total_precios)

# Ordenar los productos y precios del más barato al más caro
precios.sort()
productos.sort()
print(precios)
print(productos)

# Eliminar todos los productos y precios
print(total_productos)
precios.pop()
precios.pop()
precios.pop()
precios.pop()
precios.pop()
precios.pop()
productos.pop()
productos.pop()
productos.pop()
productos.pop()
productos.pop()
productos.pop()
print(precios)
print(productos)

