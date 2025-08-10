
class FondosInsuficientes(Exception):
    pass

saldo_disponible = 500

try:
    monto = float(input("Ingrese el monto que desea retirar: "))
    if monto > 1000:
        raise Exception("El monto excede el límite permitido")
    
    if monto > saldo_disponible:
        raise FondosInsuficientes("Fondos insuficientes para realizar el retiro")
    
    saldo_disponible = saldo_disponible - monto
    print("🎉 Retiro exitoso.")
    print("Saldo restante: ", saldo_disponible,"Bs.")

except FondosInsuficientes as e:
    print("Error en el retiro:", e)
except Exception as e:
    print("Error ocacionado:", e)