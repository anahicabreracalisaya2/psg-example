# Entrada de datos
usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")
# Diccionario de registros
usuarios_reg = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}
# Verificar datos correctos
if usuario in usuarios_reg and usuarios_reg[usuario] == contraseña :
    print("¡Acceso aprobado!")
elif usuario in usuarios_reg:
        print("Acceso denegado")
else:
    print("No existe el usuario")