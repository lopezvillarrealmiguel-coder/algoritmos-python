#problema8

kilometros = 0 # Acumula los kilometros recorridos en todas las etapas
combustible = 0 # Acumula el combustible utilizado en todas las etapas

for i in range(1,9): # Repite el ciclo para registrar 8 etapas
	print(f"Etapa {i}") # Muestra el numero de la etapa actual
	km = float(input("Ingrese la cantidad de kilometros recorridos en esta etapa:")) # Pide los kilometros recorridos
	gas = float(input("Ingresa la cantidad de combustible gastado:")) # Pide la cantidad de combustible utilizado
	kilometros += km # Suma los kilometros al total
	combustible += gas # Suma el combustible al total
	print(f"rendimiento de esta etapa es de:{km / gas}KM/L") # Divide los kilometros entre el combustible para obtener el rendimiento

print(f"\nEl total de kilometros recorridos fue de:{kilometros}") # Muestra los kilometros recorridos en total
print(f"El promedio de redimiento es de:{kilometros/combustible}") # Calcula el rendimiento general usando los totales