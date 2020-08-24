# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:38:04 2020

@author: WILLY
"""
def propagar(vector):
    #nuevo = 0
    #encendido = 1
    #carbonizado = -1
    
    anterior=0
    anterior2 = 0
    
    propagado = []
    propagado2 = []
    
    #ciclo propagacion derecha a izquierda
    for j in reversed(vector):
        if anterior2 == 1:
            if j == 0:
                j=1
                propagado2.append(j)
            else:
                propagado2.append(j)
        else:
            propagado2.append(j)
        anterior2 = j
        
    #ciclo revirtiendo y propagando de izquierda a derecha
    for i in reversed(propagado2):
        if anterior == 1:
            if i == 0:
                i=1
                propagado.append(i)
            else:
                propagado.append(i)
        else:
            propagado.append(i)
        anterior = i
    
    return propagado

vector = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]

propagado = propagar(vector)
print('propag = ' , propagado)
