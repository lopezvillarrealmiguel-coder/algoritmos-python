#PROBLEMA 20

cajas = int(input("Cuantas cajas llegaron en esta lote:"))#Numero de cajas con luces
R = 0  #Acumulador de leds rojos
V = 0  #Acumulador de leds verdes
B = 0  #Acumulador de leds blancos

for i in range (1,cajas+1):#CIclo que te pide cuantos leds de cada color llegaron en cada caja

	print(f"\nCaja {i}")
	rojos = int(input("Ingrese la cantidad de focos rojos:"))
	R += rojos
	verdes = int(input("Ingrese la cantidad de focos verdes:"))
	V += verdes
	blancos = int(input("Ingrese la cantidad de focos blancos:"))
	B += blancos



print(f"\nLa cantidad de focos rojos en esta lote fue de:{R} pz")
print(f"La cantidad de focos verdes en esta lote fue de:{V} pz")
print(f"La cantidad de focos blancos en esta lote fue de:{B} pz")
#Muesra la canidad de leds de colores en total