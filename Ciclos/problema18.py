#PROBLEMA 18

dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']#Muestra el dia en el que estas
cantdias = 7#CAntidad de dias
horas = 0#horas acumuladas
pagoxhora = float(input("cuanto se paga por hora:$"))#pago por horas extra
print ("")

for i in range(cantdias):#Ciclo que te dice el dia y la cantidad de horas trabajadas ese ia
	trahor = int(input(f"Ingrese la cantidad de horas trabajadas el dia {dias[i]}:"))
	horas += trahor

print(f"\nLa cantidad de horas trabajadas en la semana fue de:{horas}")
print(f"La paga total por {horas} es igual a:${horas*pagoxhora}")
#Muestra en texto en antalla los resultaods de las horas

