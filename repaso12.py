'''“La langosta ahumada” es una empresa dedicada a
ofrecer banquetes; sus tarifas son las siguientes: el costo
de platillo por persona es de $95.00, pero si el número de
personas es mayor a 200 pero menor o igual a 300, el
costo es de $85.00. Para más de 300 personas el costo
por platillo es de $75.00. Se requiere un algoritmo que
ayude a determinar el presupuesto que se debe presentar
a los clientes que deseen realizar un evento.
'''
per = int(input('Cuantas personas asistieron al banquete =')) # pide personas

if per <= 200:
    costo = per * 95 # $95 por persona
    print(f'El precio presupuesto que necesitan es de = {costo}')
elif per > 200 and per <= 300:
    costo = per * 85 # $85 por persona
    print(f'El precio presupuesto que necesitan es de = {costo}')
elif per > 300:
    costo = per * 75 # $75 por persona
    print(f'El precio presupuesto que necesitan es de = {costo}')