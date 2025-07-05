tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
# Convertir a conjuntos
tf= set(tienda_fisica)
to= set(tienda_online)
# a. Quiénes compraron en ambos canales.
ambos=tf.intersection(to)
print("Compraron en ambas tiendas:", ambos)
# b. Quiénes compraron solo en la tienda física.
solo_f=tf.difference(to)
print("Solo los que compraron en la tienda física son:", solo_f)
# c. Quiénes compraron solo online.
solo_o=to.difference(tf)
print("Solo los que compraron en la tienda online son:", solo_o)
