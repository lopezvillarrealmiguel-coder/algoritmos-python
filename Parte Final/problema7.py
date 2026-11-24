#problema7

temMax = 0 # Guarda la temperatura maxima registrada
temMin = 0 # Guarda la temperatura minima registrada
prom = 0 # Acumula las temperaturas para calcular el promedio


for i in range(1,31): # Repite el ciclo durante 30 dias
	temperatura = int(input(f"Ingrese la temperatura del dia {i}:")) # Pide la temperatura del dia actual
	prom += temperatura # Suma la temperatura al acumulador
	if(temperatura < temMin): # Comprueba si la temperatura es menor a la minima guardada
		temMin -= temMin # Resta el valor anterior de la temperatura minima
		temMin += temperatura # Guarda la nueva temperatura minima
	elif(temperatura > temMax): # Comprueba si la temperatura es mayor a la maxima guardada
		temMax -= temMax # Resta el valor anterior de la temperatura maxima
		temMax += temperatura # Guarda la nueva temperatura maxima


print(f"El valor minimo de temperatura fue de: °{temMin}") # Muestra la temperatura minima registrada
print(f"El valor maximo de temperatura fue de: °{temMax}") # Muestra la temperatura maxima registrada
print(f"EL promedio de temperatura fue de: °{prom/30}") # Divide la suma de temperaturas entre 30 para obtener el promedio