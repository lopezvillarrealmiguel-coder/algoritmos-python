'''
Crea una función llamada mayor_de_dos(a, b) que devuelva el
número más grande sin usar la función integrada max(). Si son
iguales, retorna cualquiera de los dos.

Prueba 1: mayor_de_dos(15, 27): 27
Prueba 2: mayor_de_dos(40, -10): 40
Prueba 3: mayor_de_dos(8, 8): 8
'''

def mayor_de_dos(a, b): # compara 2
    if a >= b: # si a es mayor
        return a
    else:
        return b # si no, b

print(mayor_de_dos(15, 27))
print(mayor_de_dos(40, -10))
print(mayor_de_dos(8, 8))