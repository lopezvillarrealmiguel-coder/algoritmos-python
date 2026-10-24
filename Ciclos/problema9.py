#PROBLEMA 9



contador = 0#Contador


for i in range (10):#Ciclo de 9 ciclos donde pide si una maleta tiene sobre peso
	pesos = float(input("Ingrese el peso de la maleta"))
	if(pesos[i]>23):
		contador += 1
		print(f"La maleta de peso {pesos[i]} tiene un peso mayor a 23")
	else:
		print("Peso regular")

print (f"El total de maletas que sobrepasan los 23Kg es de {contador}")#Muestra un texto con el numero de maletas que tienen sobrepeso
