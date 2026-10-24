#PROBLEMA 6
pares = 0#Acumuladores pares

cant = int(input("Ingrese la cantidad de numeros a colocar:"))#Ingresa la cantidad de numeros que se van a verificar

for i in range(1,cant+1):#Ciclo que toma la cantidad de numeros femuestra cuales son pares y los acumula en pares y te dice cual es par
	num = int(input(f"Ingrese el numero:{i}"))
	if num % 2 == 0:
		pares += num
		print("Este numero es par")

print(f"La suma de todos los numeros pares es de:{pares}")#Imprime la canidad de numeros pares en el intervalo de