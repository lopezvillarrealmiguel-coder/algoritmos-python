#PROBLEMA 12	

men = 0#Acumulador de numeros menores
may = 0#Acumulador de numeros mayores
equilzero = 0#Acumulador de numeros iguales a 0

	
cant = int(input("Ingrese la cantidad de numeros que desea colocar:"))#Cantidad de numeros que se van a colocar

for i in range(1,cant+1):#Ciclo que pide n cantidad de numeros y observa si son menores mayores o iguales a 0
	num = float(input(f"Ingresa el numero {i} :"))
	if(num < 0):
		men += 1
	elif(num > 0):
		may += 1
	else:
		equilzero += 1

print(f"El numero de numeros mayores a 0 son:{may}")#Imprime la cantidad de mayores
print(f"El numero de numeros menores a 0 son:{men}")#Imprime la cantidad de menores
print(f"E; numero de numeros iguales a 0 son:{equilzero}")#Imprime la cantidad deiguales a 0
