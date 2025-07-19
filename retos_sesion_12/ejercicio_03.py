# Pertenencia de autos
aut_Jhon={'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
aut_Jhess={'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
print("Los autos de Jhess son:",aut_Jhess)
print("Los autos de Jhon son:",aut_Jhon)
# verificar

comun=aut_Jhon.intersection(aut_Jhess)
cant=len(comun)
if cant > 0:
    print("Tiene",cant,"autos en común, y son:",comun )
else:
    print("No hay autos en común.")