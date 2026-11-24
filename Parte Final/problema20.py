#Problema 20


penalizacion = 0#variable acumuladora de penalizacion

facturas = int(input("Cual es el numero de facturas:"))  # Pide la cantidad de facturas que se van a procesar
for i in range (1,facturas+1):  # Repite el ciclo por cada factura
	monto = float(input(f"Cual es el monto original de la factura {i}:"))  # Pide el monto original de la factura actual
	dias_retraso = int(input(f"Cuantos dias de retraso tubo en la factura {i}:"))  # Pide los dias de retraso de la factura
	if dias_retraso > 30 and dias_retraso <= 60:  # Comprueba si el retraso es mayor a 30 y menor o igual a 60 dias
		monto1= monto*1.05 # Aumenta el monto de la factura un 5%
		penalizacion += monto1-monto # Calcula el recargo y lo suma a la penalizacion total
		print(f"Precio de factura:${monto1}") # Muestra el precio actualizado de la factura
	elif dias_retraso > 60: # Comprueba si el retraso supera los 60 dias
		monto1= monto*1.12 # Aumenta el monto de la factura un 12%
		penalizacion += monto1-monto # Calcula el recargo y lo suma a la penalizacion total
		print(f"Precio de factura:${monto1}") # Muestra el precio actualizado de la factura
	else: # Se ejecuta cuando el retraso es de 30 dias o menos
		print(f"Precio de factura igual:${monto}") # Muestra el precio original sin recargo

print(f"La acumulacion total de sus penalizacion son de:${penalizacion}")  # Muestra la cantidad total acumulada de las penalizaciones