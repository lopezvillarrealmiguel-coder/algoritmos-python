
n = int(input("coloque el numero al que quiere sacar su tabla: "))#indica el numero de la tabla a sacar

for i in range (1,11):#crea un ciclo del 1 al 11 repitiendo esto 10 veces
	
	residuo =  i*n#Crea el resultado de a multiplicacion
	print(f"{n}x{i}={residuo}")#Imprime la multiplicacion