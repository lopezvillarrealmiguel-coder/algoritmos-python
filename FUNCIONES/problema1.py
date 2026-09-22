'''
Crea una función llamada saludar(nombre) que reciba un nombre
como cadena de texto y retorne "Hola,

<nombre>!"

Prueba 1: saludar("Carlos"): "Hola, Carlos!"
Prueba 2: saludar("Ana"): "Hola, Ana!"
Prueba 3: saludar("Mundo"): "Hola, Mundo!"
'''

def saludar(nombre): # recibe nombre
    return f"Hola, {nombre}!" # arma saludo

print(saludar("Carlos"))
print(saludar("Ana"))
print(saludar("Mundo"))
