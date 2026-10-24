#PROBLEMA 14

cant = int(input("Ingrese cantidad de numeros a registrar:"))#Cantidad dde numeros a registrar
contadorMa = 0#Acumulador de menores
contadorMe = 0#Acumulador de mayores
contadorCe = 0#Acumulador de menores

for i in range(cant):#Ciclo que  va acumulando el numer pedido en la variable acumuladora respectiva
	num = float(input("Ingresa un numero:"))
	if(num < 0):
		contadorMe += 1
	elif(num > 0):
		contadorMa += 1
	else:
		contadorCe += 1

print(f"Existen ({contadorMa}) numeros mayores a 0")#Muestra la cantidad de mayores
print(f"Existen ({contadorMe}) numeros menores a 0")#Muestra la cantidad de menores
print(f"Existen ({contadorCe}) numeros iguales a 0")#Muestra la cantidad de iguales a 0
