'''
La política de la compañía telefónica “chimefón” es:
“Chismea + x -”

. Cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los
primeros cinco minutos cuestan $1.00 peso c/u, los
siguientes tres, 80¢ centavos de peso c/u, los siguientes
dos minutos, 70¢ centavos de peso c/u, y a partir del
décimo minuto, 50¢ centavos de peso c/u.
Además, se carga un impuesto de 3 % cuando es
domingo, y si es día hábil, en turno matutino, 15 %, y en
turno vespertino, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una
persona que realiza una llamada en moneda nacional
mexicana (MXN).
'''
minutos = int(input("Cuantos minutos en llamada: ")) # mins
es_domingo = int(input("Es domingo? (1=Si/0=No): ")) # dia

# costo base
if minutos <= 5:
    costo = minutos * 1 # tramo 1
elif minutos <= 8:
    costo = 5 + (minutos - 5) * 0.80 # tramo 2
elif minutos <= 10:
    costo = 7.40 + (minutos - 8) * 0.70 # tramo 3
else:
    costo = 8.8 + (minutos - 10) * 0.50 # tramo 4

# impuesto
if es_domingo == 1:
    porcentaje = 3 # domingo 3%
    tipo = "Domingo"
else:
    es_matutino = int(input("Es matutino? (1=Si/0=No): ")) # turno
    if es_matutino == 1:
        porcentaje = 15 # matutino 15%
        tipo = "Habil Matutino"
    else:
        porcentaje = 10 # vespertino 10%
        tipo = "Habil Vespertino"

impuesto = costo * (porcentaje / 100) # calcula impuesto
total = costo + impuesto # suma total

print(f"Concepto: {tipo}") # tipo
print(f"Costo base: ${costo:.2f}") # base
print(f"Impuesto ({porcentaje}%): ${impuesto:.2f}") # imp
print(f"Total a pagar: ${total:.2f}") # total