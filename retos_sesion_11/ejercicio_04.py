print("Creación de hambientes y sus especies en peligro de extinción")
ambientes = {"polo norte" : {
    "especies": {"oso polar", "morsa", "ballena"}
  }, "amazonas" : {
    "especies": {"tigre", "mono", "guacamayo"}
  }
}
print(ambientes)

# Añadir 2 habitats más 
ambientes.update({
    "desierto": {"especies": {"serpiente de cascabel", "lagarto"}},
    "sabana": {"especies": {"elefante", "león"}}
})

# Verificar si 'amazonas' existe en el diccionario
aux = "amazonas" in ambientes
print("Existe el amazonas:", aux)

# Añadir la especie 'anaconda' al 'amazonas'
ambientes["amazonas"]["especies"].add("anaconda")
print(ambientes)