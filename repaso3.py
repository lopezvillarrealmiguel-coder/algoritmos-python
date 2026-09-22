'''
Un estacionamiento requiere determinar el cobro que
debe aplicar a las personas que lo utilizan. Considere que
el cobro es con base en las horas que lo disponen y que
las fracciones de hora se toman como completas
'''
import math # para redondear hacia arriba

minutos_de_estancias = int(input("cuantos minutos estubo dentro:")) # pide minutos
precio_hora = 20 # precio por hora
redondeo = math.ceil(minutos_de_estancias / 60) # convierte min a horas y redondea
pago = redondeo * precio_hora # calcula total

print(f"Debes de pagar: {pago}") # muestra pago