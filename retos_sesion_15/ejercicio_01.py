def division(num1, num2):
    return num1 / num2

while True:
    try:
        a = input("Ingrese el primer número: ")
        if a == "salir":
            break
        b = input("Ingrese el segundo número: ")
        if b == "salir":
            break
        a = float(a)
        b = float(b)

        suma = a + b
        resta = a - b
        multi = a * b
        print("😺 Resultado de la suma: ", suma)
        print("😺 Resultado de la resta: ", resta)
        print("😺 Resultado de la multiplicación: ", multi)
        try:
            div = division(a, b)
            print("😺 Resultado de la división: ", div)
        except ZeroDivisionError as e:
            print("0️⃣ Error:", e, type(e))

    except TypeError as e:
        print(" 🤔 Error:", e, type(e))
    except Exception as e:
        print(" 😒 Error:", e, type(e))