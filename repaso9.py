'''Determina el promedio que obtendrá un alumno
considerando que realiza tres exámenes, de los cuales el
primero y el segundo tienen una ponderación de 25%,
mientras que el tercero de 50%
'''
prom1 = float(input('Dame tu primera calificacion:')) # 1ra calif
prom2 = float(input('Dame tu segunda calificacion:')) # 2da calif
prom3 = float(input('Dame tu tercera calificacion:')) # 3ra calif

prom4 = prom3 + prom3 # duplica la 3ra
calf = (prom1 + prom2 + prom4) / 4 # promedia

print(f'Tu calificacion final es {calf}') # muestra final