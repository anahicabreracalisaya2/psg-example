print("Crear una lista")
nombres = ["Anahi", "Luis", "Jose", "Marla", "Carlos", "Luisa", "Pedro", "Sofia", "Joel", "Roxana"]
print(nombres)

print("Sublista con saltos")
sub_lista = nombres[5:10:2]
print(sub_lista)

print("Busca a Jose")
print("Jose" in nombres)
print (nombres.index("Jose"))

print("Ordenar la sublista alfabéticamente de la A a la Z")
sub_lista.sort()
print(sub_lista)

print("Ordenar la lista original alfabéticamente en orden descendente Z a A")
nombres.sort(reverse=True)
print(nombres)
