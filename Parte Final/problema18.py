#Problema 18


limite = 0 # Cuenta los vehiculos que respetaron el limite de velocidad
infraccion = 0 # Cuenta los vehiculos que superaron el limite
grave = 0 # Cuenta los vehiculos que superaron los 110 km/h

for i in range(12): # Repite el ciclo para registrar 12 vehiculos
    v = float(input("Velocidad del vehículo: ")) # Pide la velocidad del vehiculo actual
    if v <= 90: # Comprueba si el vehiculo circulaba a 90 km/h o menos
        limite += 1 # Aumenta el contador de vehiculos dentro del limite
    else: # Se ejecuta cuando el vehiculo supera los 90 km/h
        infraccion += 1 # Aumenta el contador de infractores
        if v > 110: # Comprueba si la velocidad supera los 110 km/h
            grave += 1 # Aumenta el contador de infracciones graves

print("Dentro del límite:", limite) # Muestra la cantidad de vehiculos que respetaron el limite
print("Infractores:", infraccion) # Muestra la cantidad de vehiculos que cometieron una infraccion
print("Multas graves:", grave) # Muestra la cantidad de vehiculos que superaron los 110 km/h