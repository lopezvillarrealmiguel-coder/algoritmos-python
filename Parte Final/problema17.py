#problema 17

P = float(input("Monto del préstamo: ")) # Pide la cantidad total del prestamo
M = int(input("Cantidad de meses: ")) # Pide en cuantos meses se pagara el prestamo
capital = P / M # Divide el prestamo entre los meses para obtener el pago de capital mensual
saldo = P # Guarda el monto inicial que todavia se debe

for i in range(M): # Repite el ciclo por cada mes del prestamo
    interes = saldo * 0.015 # Calcula el interes del 1.5% sobre el saldo pendiente
    cuota = capital + interes # Suma el pago de capital y el interes para obtener la cuota
    saldo -= capital # Resta al saldo la cantidad de capital que ya se pago
    print("Mes:", i + 1, "Cuota:", cuota, "Saldo:", saldo) # Muestra el mes, la cuota y el saldo restante