'''Una empresa importadora desea determinar cuántos
dólares puede adquirir con equis cantidad de dinero
mexicano.
 '''

pesos = float(input("cantidad en mxn: ")) # pide los pesos
tipo_cambio = 16.96 # valor de 1 dolar en MXN

conversion = pesos / tipo_cambio # divide pesos entre el valor

print(f"en dolares es: ${conversion:.2f}") # muestra el resultado