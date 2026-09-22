'''Determina cuánto se debe pagar por equis cantidad de
lápices considerando que si son 1000 o más el costo es
de $0.85; de lo contrario, el precio es de $0.90
'''
cant = int(input("Cuantos lapices desea comprar: ")) # pide cantidad

if cant >= 1000:
    precio = cant * 0.85 # $0.85 si son 1000 o mas
    print(f'El valor de los lapices sera = {precio}')
else:
    precio = cant * 0.90 # $0.90 si son menos
    print(f'El precio de los lapices sera = {precio}')