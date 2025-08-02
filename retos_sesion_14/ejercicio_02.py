def calcular(numero1,numero2, operacion):
    if(operacion=="+"):
        sum=numero1+numero2
        return sum
    elif (operacion=="-"):
        res=numero1-numero2
        return res
    elif (operacion=="*"):
        multi=numero1*numero2
        return multi
    elif (operacion=="/"):
        if (numero2!=0):
            div=numero1/numero2
            return div
        else:
            print("Error de division")
    else:
        print("operacion invalida")

p=calcular(10,5,"+")
print("El resultado es:",p)