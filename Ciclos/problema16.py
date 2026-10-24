#PROBLEMA 16

cant = int(input("Ingrese la cantidad de ventas:"))#Ingresa la canidad de ventas
maymil = 0 #variable acumuladora de mayor a mil
maymil2 = 0 #VAriable acmuladora de total en dinero de mayores a mil
milqui = 0#variable acumuladora de mayor a 1000 a 500
milqui2 = 0#VAriable acmuladora de total en dinero de 1000 a 500
menqui = 0#variable acumuladora de menor a 500
menqui2 = 0#VAriable acmuladora de total en dinero de menores a 500
total = 0#Total en dinero de todas las compras


for i in range(1,cant+1):#Ciclo que va acumulando el dinero y cantidad de cada rango haci como te va pidiendo as ventas
	dinero = float(input(f"\nIngrese la cantidad de la venta {i}:$"))
	total += dinero
	if(dinero > 1000):
		maymil += 1
		maymil2 += dinero
	elif(dinero <= 1000 and dinero >= 500):
		milqui += 1
		milqui2 += dinero
	elif(dinero < 500):
		menqui += 1
		menqui2 += dinero

print (f"\nEl numero de ventas mayores a 1000 fueron = {maymil}")
print(f"El total de esas ventas fue de = ${maymil2}\n")
print(f"El numero de ventas de 1000 a 500 fue de = {milqui}")
print(f"El total de esas ventas fue de = ${milqui2}\n")
print(f"El numero de ventas menores de 500 fue de = {menqui}")
print(f"El total de esas ventas fue de = ${menqui2}\n")
print(f"El total general e todas las ventas fue de = ${total}")
#Muestra todas las variables acumuladoras en un texto