#problema3

acumulacion = 2000 # Guarda la cantidad inicial de dinero invertido
year = int(input("Ingrese la cantidad de años:")) # Pide los años que durara la inversion

for i in range(1, year+1): # Repite el ciclo por cada año de inversion
    acumulacion *= 1.08 # Aumenta el dinero un 8% cada año
    print(f"La inversion en el año {i} fue de: ${acumulacion}") # Muestra cuanto dinero se tiene al terminar cada año