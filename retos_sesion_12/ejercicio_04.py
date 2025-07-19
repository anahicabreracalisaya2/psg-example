print("Bienvenido a la tienda ingrese sus datos para verificar su descuento")
edad=int(input("Ingrese su edad: "))
compra=int(input("Ingrese el valor de su compra: "))
if edad>=60 and compra>1000:
    saldo1=compra-(compra*0.20)
    print("Su descuento es del 20%, ahora su saldo es:",saldo1 )
elif 18<= edad <60 and compra>500:
    saldo2=compra-(compra*0.10)
    print("Su descuento es del 10%, ahora su saldo es:",saldo2 )
else:
    saldo3=compra-(compra*0.02)
    print("Su descuento es del 2%, ahora su saldo es:",saldo3)