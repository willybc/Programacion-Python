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
vector = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]

invertida = invertir_lista(lista)
print('inversion de lista = ' , invertida)

invertida = invertir_lista(vector)
print('inversion de vector = ' , invertida)