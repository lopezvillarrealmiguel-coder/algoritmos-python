#PROBLEMA 7



menor = 0#Acumulador de numeros menores

for i in range(1,9):#Ciclo de acumulador de numeros colocados indicando si son menores o mayores
	edad = int(input(f"Persona {i} Ingrese su edad"))
	if(edad < 18):
		menor += 1
	else:
		menor +=0

print(f"El numero de personas menores de edad es de {menor}")#Te muestra un texto de cuantos numeros ueron menores
