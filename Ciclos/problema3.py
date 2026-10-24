#PROBLEMA 3

suma = 0#Variable para acumular valores
cant = 5#cantidad de numeros que se suman

for i in range(1,cant+1):#Ciclo de 1 a 6
	num = int(input(f"Ingrese el numero{i}:"))#El susurio coloca los 5 numeros
	suma =+ num#se suma las cantidades que ponga e usuario y se guarda en suma

print(f"La suma de todos los numeros es:{suma}")#Imprime la suma de todos os numeros