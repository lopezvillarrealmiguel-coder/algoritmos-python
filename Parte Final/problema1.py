#problema1

salario = 0 # Variable que guarda el dinero acumulado de la semana
pagoXh = 60 # Cantidad que se paga por cada hora normal
hextra = 0 # Variable que acumula las horas extras trabajadas
dia = ('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado') # Lista con los dias de trabajo

for i in range(0, 6): # Ciclo que se repite 6 veces, una por cada dia
    h = int(input(f"Ingrese las horas trabajadas en el dia {dia[i]} ")) # Pide las horas trabajadas en el dia actual

    if(h <= 8): # Comprueba si trabajo 8 horas o menos
        salario += pagoXh*h # Multiplica las horas por el pago normal y lo suma al salario
    elif(h > 8): # Comprueba si trabajo mas de 8 horas
        salario += pagoXh*8 # Calcula el pago de las primeras 8 horas
        doble = h-8 # Calcula cuantas horas extras trabajo
        salario += (pagoXh*2)*doble # Paga las horas extras al doble
        hextra += doble # Guarda las horas extras acumuladas

print(f"El salario total de la semana es de :${salario}") # Muestra el salario total
print(f"La cantidad de horas extra son de {hextra}") # Muestra el total de horas extras