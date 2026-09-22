'''
Diseña una función llamada area_triangulo(base, altura) que
calcule el área mediante la fórmula (base x altura) / 2 y valide que
ambos valores sean mayores a cero; si no lo son, debe retornar
0.

Prueba 1: area_triangulo(10, 5): 25.0
Prueba 2: area_triangulo(7, 4): 14.0
Prueba 3: area_triangulo(-2, 5): 0
'''

def area_triangulo(base, altura): # base y altura
    if base <= 0 or altura <= 0: # valida positivos
        return 0
    else:
        return (base * altura) / 2 # formula

print(area_triangulo(10, 5))
print(area_triangulo(7, 4))
print(area_triangulo(-2, 5))