'''
Almacenes “El harapiento distinguido” tiene una
promoción: a todos los trajes que tienen un precio
superior a $2500.00 se les aplicará un descuento de 15 %,
a todos los demás se les aplicará sólo 8 %. Realice un
algoritmo para determinar el precio final que debe pagar
una persona por comprar un traje y de cuánto es el
descuento que obtendrá.
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