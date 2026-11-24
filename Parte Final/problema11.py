#problema11

personas = int(input("Ingrese la cantidad de personas ")) # Pide la cantidad de personas que se van a registrar
niños = 0 # Cuenta a las personas de entre 1 y 12 años
adolescentes = 0 # Cuenta a las personas de entre 13 y 17 años
adultos = 0 # Cuenta a las personas de entre 18 y 59 años
adultoM = 0 # Cuenta a las personas de 60 años o mas

for i in range(1,personas+1): # Repite el ciclo por cada persona
	edad = int(input("Ingrese su edad actual")) # Pide la edad de la persona actual
	if(edad <= 12 and edad >= 1) # Comprueba si la edad esta entre 1 y 12 años
		niños += 1 # Aumenta el contador de niños
	elif(edad <= 17 and edad >= 13) # Comprueba si la edad esta entre 13 y 17 años
		adolescentes += 1 # Aumenta el contador de adolescentes
	elif(edad <= 59 and edad >= 18) # Comprueba si la edad esta entre 18 y 59 años
		adultos += 1 # Aumenta el contador de adultos
	elif(edad >= 60) # Comprueba si la persona tiene 60 años o mas
		adultos += 1 # Aumenta el contador indicado en el codigo

print(f"\nRegistros") # Muestra el titulo de los resultados
print(f"niños ={niños}") # Muestra la cantidad de niños
print(f"adolescentes ={adolescentes}") # Muestra la cantidad de adolescentes
print(f"adultos ={adultos}") # Muestra la cantidad de adultos
print(f"adultos mayores ={adultoM}") # Muestra la cantidad de adultos mayores