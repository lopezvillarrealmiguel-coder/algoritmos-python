#problema12


ventas = int(input("Cantidad de ventas: ")) # Pide la cantidad de ventas realizadas
total = 0 # Acumula el dinero ganado por las comisiones
mayor = 0 # Guarda el monto de la venta mas grande

for i in range(ventas): # Repite el ciclo por cada venta
    venta = float(input("Monto de venta: ")) # Pide el monto de la venta actual
    if venta > 1500: # Comprueba si la venta supera los 1500 pesos
        total += venta * 0.10 # Calcula una comision del 10% y la suma al total
    elif venta >= 500: # Comprueba si la venta es de 500 o mas y no supera los 1500
        total += venta * 0.05 # Calcula una comision del 5% y la suma al total
    if venta > mayor: # Comprueba si la venta actual es mayor a la guardada
        mayor = venta # Guarda el nuevo monto de venta mas grande

print("Total de comisiones:", total) # Muestra el dinero total ganado por comisiones
print("Mayor venta:", mayor) # Muestra el monto de la venta mas grande