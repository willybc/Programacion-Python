# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:24:04 2020

@author: wilfr
"""

def hojas(N, ancho = 841, largo = 1189):

    if N == 0:
        return ancho, largo

    elif N == 1:
        return largo/2, ancho

    else:
        return hojas(N - 1, largo/2, ancho)
    
for i in range(11):
    ancho, largo = hojas(i)
    print(f'Hoja A{i} ; Ancho: {ancho} ; Largo: {largo}')
