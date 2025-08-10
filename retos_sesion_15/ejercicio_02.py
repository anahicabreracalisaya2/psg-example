class NoFrutaError(Exception):
    pass
fruta_permitida = {"🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"}
canasta = []

while True:
    try:
        fruta = input("Ingrese una fruta: ")
        if fruta == "salir":
            print("Mi frutero contiene:", canasta)
            break
        if fruta not in fruta_permitida:
            raise NoFrutaError("Esta no es una fruta") 
        canasta.append(fruta)
    except NoFrutaError as e:
        print("🍃 Error frutal:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Fruta agregada")


        
