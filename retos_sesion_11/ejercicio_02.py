#Crear el diccionario
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
# Incrementa alimentos
alimentos.update(
    {'pollo':["gato", "perro"],"pescado":"pez", "lechuga":["conejo", "caballo"],"trigo":["paloma", "pato"]}
)
print(alimentos)
# Verificar si 'trigo' está en el diccionario
existe_trigo = "trigo" in alimentos
print("Se encuentra el trigo:", existe_trigo)
# Eliminar 'zanahoria' del diccionario
alimentos.pop("zanahoria") 
print("Este es el nuevo diccionario:", alimentos)