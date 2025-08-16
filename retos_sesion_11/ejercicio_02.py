#Crear el diccionario
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
# Incrementa alimentos
alimentos.update(
    pollo=["gato", "perro"],
    pescado="delfines",
    lechuga=["conejo", "caballo"],
    trigo=["paloma", "pato"]
)
print("Ahora la lista es: \n",alimentos)
# Verificar si 'trigo' está en el diccionario
existe_trigo = "trigo" in alimentos
print("Se encuentra el trigo:", existe_trigo)

# Eliminar 'zanahoria' del diccionario
alimentos.pop("zanahoria") 
print("Este es el nuevo diccionario sin zanahoria:", alimentos)