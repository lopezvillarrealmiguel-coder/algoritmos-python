'''
La política de la compañía telefónica “chimefón” es:
“Chismea + x -”

. Cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los
primeros cinco minutos cuestan $1.00 peso c/u, los
siguientes tres, 80¢ centavos de peso c/u, los siguientes
dos minutos, 70¢ centavos de peso c/u, y a partir del
décimo minuto, 50¢ centavos de peso c/u.a (MXN).
Determinar cuánto debe pagar por cada concepto una
persona que realiza una llamada en moneda nacional
mexicana (MXN).
'''
minutos = int(input("Cuantos minutos a estado en llamada solo deme minutos:")) # pide minutos

if minutos <= 5:
    costo = minutos * 1 # $1 por min
    print(f"El costo total de su llamada es de: ${costo}")
elif minutos > 5 and minutos <= 8:
    minu = minutos - 5 # mins extra
    costo = 5 + (minu * .80) # base + $0.80
    print(f"El costo total de su llamada es de: ${costo}")
elif minutos > 8 and minutos <= 10:
    minu = minutos - 8 # mins extra
    costo = 7.40 + (minu * .70) # base + $0.70
    print(f"El costo total de su llamada es de: ${costo}")
elif minutos > 10:
    minu = minutos - 10 # mins extra
    costo = 8.8 + (minu * .50) # base + $0.50
    print(f"El costo total de su llamada es de: ${costo}")