#PROBLEMA 5

pares = 0#Acumula cuantos pares hay de 1 a 20
for i in range(1,21):#Crea un ciclo que en caso de qu un numero de 1 al 20 se par se acumula en pares
	if i % 2 == 0:
		print(i)
		pares += 1

print(f"El numero total de pares es {pares}")#IMprime los pares
