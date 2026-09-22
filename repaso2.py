
''' Una empresa que contrata personal requiere determinar la
edad de las personas que solicitan trabajo, pero cuando
se les realiza la entrevista sólo se les pregunta el año en
que nacieron.
'''
edad = int(input("Dime tu año de nacimiento: ")) # pide año

age = 2026 - edad # resta año actual menos año de nacimiento

print(f"La persona tiene {age}") # muestra la edad