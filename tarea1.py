'''
El director de una escuela está organizando un viaje de
estudios, y requiere determinar cuánto debe cobrar a
cada alumno y cuánto debe pagar a la compañía de viajes
por el servicio. La forma de cobrar es la siguiente: si son
100 alumnos o más, el costo por cada alumno es de
$65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30
a 49, de $95.00, y si son menos de 30, el costo de la
renta del autobús es de $4000.00, sin importar el
número de alumnos.
'''

precio = float(input("Ingresa el precio del traje: $")) # pide precio

if precio > 2500:
    porcentaje = 15 # 15% si pasa de 2500
else:
    porcentaje = 8 # 8% si no

descuento = precio * (porcentaje / 100) # calcula descuento
precio_final = precio - descuento # resta descuento

print(f"Precio original: ${precio:.2f}") # muestra precio original
print(f"Descuento aplicado: {porcentaje}% = ${descuento:.2f}") # muestra descuento
print(f"Precio final a pagar: ${precio_final:.2f}") # muestra total
