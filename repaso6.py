'''
Se requiere determinar el costo que tendrá realizar una
llamada telefónica con base en el tiempo que dura la
llamada y en el costo por minuto.

costo por minuto: $3.00 mxn
'''

min = int(input("Cuantos minutos estubo en llamada:")) # pide minutos

precio = 3 * min # $3 por minuto

print(f"Debera pagar un total de : ${precio}") # muestra total
