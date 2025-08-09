def division(num1, num2):
    return num1 / num2

while True:
    try:
        a = float(input("Ingrese el primer número: "))
        if a == "salir":
            break
        b = float(input("Ingrese el segundo número: "))
        if b == "salir":
            break
        suma=a+b
        resta=a-b
        multi=a*b
        div = division(a, b)
    except ZeroDivisionError as e:
        print("0️⃣ Error:", e, type(e))
    except TypeError as e:
        print(" 🤔 Error:", e, type(e))
    except Exception as e:
        print(" 😒 Error:", e, type(e))
    else:
        print("😺 Resultado de la suma: ",suma)
        print("😺 Resultado de la resta: ",resta)
        print("😺 Resultado de la multiplicacion: ",multi)
        print("😺 Resultado de la division: ",div)
        