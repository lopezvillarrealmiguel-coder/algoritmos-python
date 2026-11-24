#problema4

meta = int(input("Ingrese la meta a vencer: $")) # Pide la cantidad de dinero que se quiere alcanzar
acumulacion = 0 # Variable que guarda el dinero acumulado
mes = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre') # Guarda los nombres de los meses

for i in range(0, 12): # Repite el ciclo 12 veces, una por cada mes
    dinero = int(input(f"Ingrese la cantidad del mes {mes[i]}: ")) # Pide el dinero obtenido durante el mes
    acumulacion += dinero # Suma el dinero del mes al total acumulado
    print(f"La acumulacion hasta {mes[i]} es de: ${acumulacion}") # Muestra el dinero acumulado hasta ese mes