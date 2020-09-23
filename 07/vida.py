# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:59:24 2020

@author: WILLY
"""

'''
Funcion que le pasas una fecha de nacmiento como
cadena en formato dd/mm/AAAA (separados con barras normales)
y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs)
'''
from datetime import date

def segundos_vividos(fecha):
    fecha_hoy = date.today()
    dias = fecha_hoy - fecha
    segundos = dias.total_seconds()
    return segundos

fecha_nacimiento = date(1996,6,30)
segundos = segundos_vividos(fecha_nacimiento)
