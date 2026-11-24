#problema10

cant = int(input("Ingrese la cantidad de promedio que avaluara:")) # Pide la cantidad de promedios que se van a evaluar
reprobado = 0 # Cuenta los alumnos que reprobaron
aprobado = 0 # Cuenta los alumnos que aprobaron
excelencia = 0 # Cuenta los alumnos con promedio de excelencia
promgen = 0 # Acumula todos los promedios para calcular el promedio general

for i in range(1,cant+1): # Repite el ciclo por cada promedio
	prom = float(input(f"Coloque el promedio {i}:")) # Pide el promedio del alumno actual
	promgen += prom # Suma el promedio al acumulador general
	if(prom < 6): # Comprueba si el promedio es menor a 6
		reprobado += 1 # Aumenta el contador de alumnos reprobados
	elif(prom > 6 and prom < 9): # Comprueba si el promedio esta entre 6 y 9
		aprobado += 1 # Aumenta el contador de alumnos aprobados
	elif(prom < 10): # Comprueba si el promedio es menor a 10 y no entro en las condiciones anteriores
		excelencia += 1 # Aumenta el contador de alumnos con excelencia

print(f"\nLa cantidad de promedio de excelencia es de:{excelencia}") # Muestra la cantidad de alumnos con excelencia
print(f"La cantidad de promedio de aprobado es de:{aprobado}") # Muestra la cantidad de alumnos aprobados
print(f"La cantidad de promedio de reprobado es de:{reprobado}") # Muestra la cantidad de alumnos reprobados
print(f"El promedio total de el salon es de:{promgen/cant}") # Divide la suma de los promedios entre la cantidad de alumnos