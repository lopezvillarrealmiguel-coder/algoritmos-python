'''Se requiere determinar cuál de tres cantidades
proporcionadas es la mayor.
'''
num1 = float(input("Escribe el primer numero: ")) # pide 1
num2 = float(input("Escribe el segundo numero: ")) # pide 2
num3 = float(input("Escribe el tercero numero: ")) # pide 3

if num1 > num2 and num1 > num3:
    print('el primer numero es el mayor') # numero alto 1
elif num2 > num3 and num2 > num1:
    print('el segundo numero es el mayor') # numero alto 2
elif num3 > num2 and num3 > num1:
    print('el tercero numero es el mayor') # numero alto 3
else:
    print('Existe mas de un numero mayor') # empate