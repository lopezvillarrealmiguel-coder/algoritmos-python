#PROBLEMA 19

salario = 1500#Salario pagado 
year = 6#cantidad de años

for i in range(1,year + 1):#Ciclco que va aumentando un 10% cada año e impre la cantidad que se acumula cada año
	salario  += (salario*(.1))
	print(f"El salario en el año transcurrido numero {i} es de:{salario}")
