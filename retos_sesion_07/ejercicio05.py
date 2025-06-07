cadena = input("Ingresa una cadena: ")
cadena_limpia = cadena.replace(" ", "").lower()
print(cadena_limpia[::-1])
es_palindromo = cadena_limpia == cadena_limpia[::-1]

print("Esta palabra es palindromo:", es_palindromo)