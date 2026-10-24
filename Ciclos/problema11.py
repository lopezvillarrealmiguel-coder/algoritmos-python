#PROBLEMA 11

pesos = [23,24,15,40,20,10,13,15,12,8]#Indica que existen 10 valores n esta variable

contador = 0#Variable donde se acumulara el sobrepeso


for i in range (10):#ciclo que indica cuales de los pesos de las variables tiene sobrepeso
	print(pesos[i])
	if(pesos[i]>23):
		contador += 1
		print(f"La maleta de peso {pesos[i]} tiene un peso mayor a 23")

print (f"El total de maletas que sobrepasan los 23Kg es de {contador}")#Muestra el total de maletas con sobrepeso

