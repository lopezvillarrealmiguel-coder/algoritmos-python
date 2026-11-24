#problema5


box = int(input("Ingrese la cantidad de cajas que entraron a la bodega:")) # Pide la cantidad de cajas que llegaron
electronicos = 0 # Acumula la cantidad de productos electronicos
ropa = 0 # Acumula la cantidad de productos de ropa
alimentos = 0 # Acumula la cantidad de productos alimenticios

for i in range (1,box+1): # Repite el ciclo por cada caja recibida
	print(f"\nCaja numero {i}") # Muestra el numero de la caja actual
	el = int(input("Ingrse la cantidad de productos electronicos de esta caja:")) # Pide la cantidad de electronicos de la caja
	electronicos += el # Suma los electronicos al total
	ro = int(input("Ingrse la cantidad de productos de ropa de esta caja:")) # Pide la cantidad de ropa de la caja
	ropa += ro # Suma la ropa al total
	al = int(input("Ingrse la cantidad de productos alimenticios de esta caja:")) # Pide la cantidad de alimentos de la caja
	alimentos += al # Suma los alimentos al total

total = electronicos + ropa + alimentos	# Suma todos los productos para obtener el total
porele = (electronicos / total)*100 # Calcula el porcentaje que representan los electronicos
print(f"\nCantidad de productos electronicos :{electronicos}") # Muestra la cantidad total de electronicos
print(f"Porcentaje que ocupan en la bodega:{porele}%") # Muestra el porcentaje de electronicos
porro =	(ropa / total)*100 # Calcula el porcentaje que representa la ropa
print(f"\nCantidad de productos vestimenta :{ropa}") # Muestra la cantidad total de ropa
print(f"Porcentaje que ocupan en la bodega:{porro}%") # Muestra el porcentaje de ropa
poral =	(alimentos / total)*100 # Calcula el porcentaje que representan los alimentos
print(f"\nCantidad de productos alimenticios :{alimentos}") # Muestra la cantidad total de alimentos
print(f"Porcentaje que ocupan en la bodega:{poral}%") # Muestra el porcentaje de alimentos