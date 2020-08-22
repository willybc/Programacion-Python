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
        
            #0      1          -1
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


lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
vector = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
invertida = invertir_lista(lista)
propagado = propagar(vector)

print('vector = ' ,vector)
print('propag = ' , propagado)

    