# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:38:04 2020

@author: WILLY
"""

def invertir_lista(lista):
    invertida = []
    cont=0
    for e in reversed(lista):
        invertida.append(e)
    return invertida



lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
invertida = invertir_lista(lista)


for i in invertida:
    print(i)


    
