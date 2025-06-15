cadena = input("Ingresa una cadena: ")
cadena_limpia = cadena.replace(" ", "").lower()
es_palindromo = cadena_limpia == cadena_limpia[::-1]

print(cadena,"es", es_palindromo)