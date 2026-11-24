#problema6

paquetes = int(input("Ingresa la cantidad de paquetes que ingreasaron al almacen:")) # Pide la cantidad de paquetes recibidos
sobrepeso = 0 # Cuenta los paquetes que superan el peso permitido
recargo = 0 # Acumula el dinero que se cobrara por sobrepeso

for i in range(1,paquetes+1): # Repite el ciclo por cada paquete
	peso = float(input(f"Ingresa el peso del paquete {i}:")) # Pide el peso del paquete actual

	if(peso > 15): # Comprueba si el peso supera los 15 kilos
		sobrepeso += 1 # Aumenta el contador de paquetes con sobrepeso
		recargo += 50 # Suma 50 pesos al recargo total

print(f"El numero de maletas que exeden el peso fueron:{sobrepeso}") # Muestra la cantidad de paquetes con sobrepeso
print(f"El recargo total por todas las maletas que exeden el peso sera de:${recargo}") # Muestra el dinero total de los recargos