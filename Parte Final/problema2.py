#problema2

cantMentrecientos = 0 # Cuenta las compras menores a 300
CMT = 0 # Acumula el dinero de las compras menores a 300
cantOchoytres = 0 # Cuenta las compras entre 300 y 800
COT = 0 # Acumula el dinero de las compras entre 300 y 800
cantMayorochocientos = 0 # Cuenta las compras mayores a 800
CMO = 0 # Acumula el dinero de las compras mayores a 800

ventas = int(input("Ingresa la cantidad de ventas:")) # Pide la cantidad de ventas que se van a registrar

for i in range(1, ventas+1): # Repite el ciclo segun la cantidad de ventas
    compra = float(input(f"Ingrese el monto de la compra numero {i}: $")) # Pide el monto de cada compra

    if(compra < 300): # Comprueba si la compra es menor a 300
        cantMentrecientos += 1 # Aumenta el contador de compras menores a 300
        CMT += compra # Suma el monto de la compra
    elif(compra >= 300 and compra <= 800): # Comprueba si esta entre 300 y 800
        cantOchoytres += 1 # Aumenta el contador de compras de este rango
        COT += compra # Suma el monto de la compra
    elif(compra > 800): # Comprueba si la compra supera los 800
        cantMayorochocientos += 1 # Aumenta el contador de compras mayores a 800
        CMO += compra # Suma el monto de la compra

print(f"\nEl total de compras menores a 300 fue de: {cantMentrecientos}") # Muestra cuantas compras fueron menores a 300
print(f"El total monetario de ventas por debajo de 300 fue de: ${CMT}") # Muestra el dinero acumulado de esas compras
print(f"\nEl total de compras entre 300 y 800 fue de: {cantOchoytres}") # Muestra cuantas compras estuvieron en ese rango
print(f"El total monetario de ventas de 300 a 800 fue de: ${COT}") # Muestra el dinero acumulado de ese rango
print(f"\nEl total de compras mayores a 800 fue de: {cantMayorochocientos}") # Muestra cuantas compras superaron los 800
print(f"El valor monetario de ventas mayores a 800 fue de: ${CMO}") # Muestra el dinero acumulado de esas compras