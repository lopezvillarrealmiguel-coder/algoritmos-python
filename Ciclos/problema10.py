#PROBLEMA 10

edad = [18,29,15,25,23,27,16,17]#Indica varios valores en una variable
contador = 0#Acumulador de sobrepeso

for i in range(8):#Ciclo que indica si entre los valores de edad hay menres de edad
	print(edad[i])
	if(edad[i]<18):
		contador += 1
		print(f"Tienes {edad[i]} eres menor de edad")

print (f"\nHay {contador} personas menores de edad")#Muestra el contador de menores de edad
