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
    nuevo = 0
    encendido = 1
    carbonizado = -1
    
    anterior=0
    
    propagado = []
    propagado2 = []
    propagado3 = []
    
    
    #ciclo  propagacion izq a derecha
    for i in (vector):
        if anterior == 1:
            if i == 0:
                i=1
                propagado.append(i)
            else:
                propagado.append(i)
        else:
            propagado.append(i)
        anterior = i
    
    anterior2 = 0
    
    #ciclo propagacion derecha a izquierda
    for j in reversed(propagado):
        if anterior2 == 1:
            if j == 0:
                j=1
                propagado2.append(j)
            else:
                propagado2.append(j)
        else:
            propagado2.append(j)
        anterior2 = j
    
    #revirtiendo el orden del ciclo anterior
    for l in reversed(propagado2):
        propagado3.append(l)
    
    return propagado3


lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
vector = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
invertida = invertir_lista(lista)
propagado = propagar(vector)

print('vector = ' ,vector)
print('propag = ' , propagado)

    