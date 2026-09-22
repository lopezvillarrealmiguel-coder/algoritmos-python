'''
Determina cuánto pagará finalmente una persona por un
artículo equis, considerando que tiene un descuento de
20%, y debe pagar 15% de IVA (debe mostrar el precio con
descuento y el precio final).

Crea un menú para que el usuario elija entre 2 productos y
el que elija, despliegua el nombre de producto, precio,
precio con descuento y precio final.
''' 
print('escoge 1 para coca') # menu 1
print('escoge 2 para galletas maria') # menu 2
escoge = int(input("escoge un producto: ")) # pide opcion

if escoge == 1:
    articulo = 27 # precio coca
else:
    articulo = 8 # precio galletas

des = articulo * 0.20 # 20% descuento
art = articulo - des # precio con descuento

iva = art * 0.15 # 15% iva
total = art + iva # total a pagar

print(f"su articulo con descuento es de: {art}") # muestra con descuento
print(f"usted debera pagar con iva: {total}") # muestra total