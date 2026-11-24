#Problema 15

total = 0 # Variable que acumula el gasto de los seis bimestres

for i in range(6): # Repite el ciclo 6 veces, una por cada bimestre
    kwh = float(input("Consumo en kWh: ")) # Pide la cantidad de energia consumida
    if kwh <= 250: # Comprueba si el consumo es de 250 kWh o menos
        pago = kwh * 1.5 # Calcula el pago usando la tarifa de 1.5 pesos
    else: # Se ejecuta cuando el consumo supera los 250 kWh
        pago = 250 * 1.5 + (kwh - 250) * 2.8 # Cobra los primeros 250 kWh a 1.5 y el exceso a 2.8

    total += pago # Suma el pago del bimestre al gasto total
    print("Pago del bimestre:", pago) # Muestra el importe que se debe pagar en ese bimestre

print("Gasto anual:", total) # Muestra el gasto total de los seis bimestres