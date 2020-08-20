# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:40:56 2020

@author: WILLY
"""

def buscar_u_elemento(lista, elemento):
    pos = -1
    for i , j in enumerate(lista):
        if j == elemento:
            pos = i
            
    return pos

def buscar_n_elemento(lista, elemento):
    contador = 0
    for i, j in enumerate(lista):
        if j == elemento:
            contador += 1
    
    return contador

lista = [1,2,3,2,3,4]
buscar_u_elemento(lista, 5)

buscar_n_elemento(lista, 2)


