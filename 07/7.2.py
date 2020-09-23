# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:37:27 2020

@author: WILLY
"""

'''
Programa que asiste a los tecnicos,
al correr el programa el numero que deben
poner en la placa
'''

#Asumiendo que estamos en el hemisferio sur

from datetime import date

hoy = date.today()
"""
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Dia actual:', hoy.day)
print('Dia de la semana:', hoy.weekday())
"""
a = date(2020, 9, 20)
inicio_primavera = date(2020, 9, 22)
fin_primavera = date(2020,12,21)

if hoy >= inicio_primavera and hoy <= fin_primavera:
    print('Ya es primavera!')
else:
    falta = inicio_primavera - a
    print(falta)
