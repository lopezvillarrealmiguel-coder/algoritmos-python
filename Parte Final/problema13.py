#problema13

M = T = N = 0 # Inicializa los acumuladores de produccion de los tres turnos

for d in range(7): # Repite el ciclo durante los 7 dias de la semana
    print("Día", d + 1) # Muestra el numero del dia actual
    M += int(input("Producción mañana: ")) # Pide y acumula la produccion del turno de mañana
    T += int(input("Producción tarde: ")) # Pide y acumula la produccion del turno de tarde
    N += int(input("Producción noche: ")) # Pide y acumula la produccion del turno de noche

print("Mañana:", M) # Muestra la produccion total del turno de mañana
print("Tarde:", T) # Muestra la produccion total del turno de tarde
print("Noche:", N) # Muestra la produccion total del turno de noche

if M > T and M > N: # Comprueba si mañana produjo mas que tarde y noche
    print("Turno más productivo: Mañana") # Muestra que mañana fue el turno mas productivo
elif T > M and T > N: # Comprueba si tarde produjo mas que mañana y noche
    print("Turno más productivo: Tarde") # Muestra que tarde fue el turno mas productivo
elif N > M and N > T: # Comprueba si noche produjo mas que mañana y tarde
    print("Turno más productivo: Noche") # Muestra que noche fue el turno mas productivo
else: # Se ejecuta cuando no existe un turno que supere a los otros dos
    print("Hay empate") # Muestra que hay un empate en la produccion