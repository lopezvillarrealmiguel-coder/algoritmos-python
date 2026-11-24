#problema14

N = int(input("Cantidad de productos: ")) # Pide la cantidad de productos que se van a registrar
total = 0 # Acumula el aumento de precio de todos los productos

for i in range(N): # Repite el ciclo por cada producto
    precio = float(input("Precio actual: ")) # Pide el precio actual del producto
    if precio < 100: # Comprueba si el precio es menor a 100 pesos
        nuevo = precio * 1.05 # Aumenta el precio un 5%
    elif precio <= 500: # Comprueba si el precio esta entre 100 y 500 pesos
        nuevo = precio * 1.08 # Aumenta el precio un 8%
    else: # Se ejecuta cuando el precio supera los 500 pesos
        nuevo = precio * 1.12 # Aumenta el precio un 12%

    diferencia = nuevo - precio # Calcula cuanto aumento el precio del producto
    total += diferencia # Suma el aumento al total acumulado
    print("Anterior:", precio, "Nuevo:", nuevo) # Muestra el precio anterior y el nuevo precio

print("Aumento total:", total) # Muestra la suma de todos los aumentos