# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:20:44 2020

@author: WILLY
"""

import datetime

#Obtener fecha y hora actual
fecha_hora = datetime.datetime.now()
print(fecha_hora)

#Fecha actual
fecha = datetime.date.today()
print(fecha)

#Objeto para representar fecha
d = datetime.date(2020,9,23)
print(d)

#fecha timestamp
from datetime import date
timestamp = date.fromtimestamp(1)
print('Fecha = ', timestamp)

#Obtener el año , mes y el dia por separado
hoy = date.today()
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Dia actual:', hoy.day)
print('Dia de la semana:', hoy.weekday()) #va de 0 a 6 empezando en lunes

#Clase datetime.time
from datetime import time

a = time()
print('a =', a)

b = time(11,34,56)
print('b =', b)

c = time(hour=11, minute=34, second=56)
print('c =', c)

#Obtener horas, minutos, segundos
a = time(11,34,56)
print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond) #predeterminado = 0

#Obtener año,mes,dia, hora, minutos con timestamp 
from datetime import datetime
a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())


