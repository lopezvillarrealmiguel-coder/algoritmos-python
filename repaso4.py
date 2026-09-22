'''
La compañía de autobuses “La curva loca” requiere
determinar el costo que tendrá el boleto de un viaje
sencillo, esto basado en los kilómetros por recorrer y en
el costo por kilómetro.

Costo por km: $80.00 mxn
'''

KMRE = int(input("Dime cuantos kilometros vas a viajar:")) # pide km
costoKM = 80 # costo por km
pago = KMRE * costoKM # multiplica km x costo

print(f"Debes de pagar: {pago}") # muestra total