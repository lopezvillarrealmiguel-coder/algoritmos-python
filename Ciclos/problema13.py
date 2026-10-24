#PROBLEMA 13


meses = ['Enero','Febrero','Marzo','Abril',"Mayo","Junio","Julio",'Agosto','Septiembre','Octubre','Noviembre','Diciembre',]#variables de tipo string que demuestran los meses
mes = 12#Indica la cantidad de meses
ahorro = 0 #Idica la Acumulacion de ahorro

for i in range(mes):#Ciclo que muestra el mes pide cuanto dinero ahorraste este mes y acumula el ahorro e imprime cuanto lleva ahorrado
	print(meses[i])
	dinero = float(input(f"Ingrese la cantidad ingresada en el mes de {meses[i]}"))
	ahorro += dinero
	print(f'Hasta el mes de {i} a ahorrado ${ahorro}')