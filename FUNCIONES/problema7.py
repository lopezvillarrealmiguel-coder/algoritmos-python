'''
Escribe una función llamada es_mayor_de_edad(edad) que reciba
un entero y retorne "Mayor" si tiene 18 años o más, y "Menor" en
caso contrario.

Prueba 1: es_mayor_de_edad(17): "Menor"
Prueba 2: es_mayor_de_edad(18): "Mayor"
Prueba 3: es_mayor_de_edad(45): "Mayor"
'''

def es_mayor_de_edad(edad): # recibe edad
    if edad >= 18: # valida 18
        return "Mayor"
    else:
        return "Menor"

print(es_mayor_de_edad(17))
print(es_mayor_de_edad(18))
print(es_mayor_de_edad(45))