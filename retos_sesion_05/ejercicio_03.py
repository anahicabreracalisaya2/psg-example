segundos= 1000000
# Constantes p
segundos_en_un_minuto= 60
segundos_en_una_hora = 60 * segundos_en_un_minuto
segundos_en_un_dia = 24 * segundos_en_una_hora 
segundos_en_una_semana = 7 * segundos_en_un_dia

# Cálculo de semanas
semanas = segundos / segundos_en_una_semana
resto = segundos % segundos_en_una_semana

# Cálculo de días
dias = resto / segundos_en_un_dia
resto = resto % segundos_en_un_dia

# Cálculo de horas
horas = resto / segundos_en_una_hora
resto = resto % segundos_en_una_hora

# Cálculo de minutos
minutos = resto / segundos_en_un_minuto

# Cálculo de segundos restantes
segundosr= resto % segundos_en_un_minuto
semanas=int(semanas)
dias=int(dias)
horas=int(horas)
minutos=int(minutos)

# Mostrar resultado
print(segundos)
print("son equivalentes a semanas:")
print(semanas)
print("son equivalentes a días:")
print(dias)
print("son equivalentes a horas:")
print(horas)
print("son equivalentes a minutos:")
print(minutos)
print("son equivalentes a segundos:")
print(segundos)
