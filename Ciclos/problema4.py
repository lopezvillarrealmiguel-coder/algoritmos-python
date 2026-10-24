#PROBLEMA 4

suma = 0#Variable acumuladora
cant = int(input("Ingrese la cantidad de numeros"))#Ingresa el usario la cantidad de numeros que colocara

for i in range(1,cant+1):#Ciclos de repeticiones de codigo
	num = int(input(f"Ingrese el numero{i}:"))#Ingresa los numeros
	suma =+ num#acumula la cantidad de numeros en esta variable

print(f"La suma de todos los numeros es:{suma}")#Envia texto a la pantalla de la acumulacion de os numeros