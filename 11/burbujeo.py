# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:09:31 2020

@author: wilfr
"""
#range(start, stop, step)
def ord_burbujeo(lista):
    intercambios = True
    numPasados = len(lista)-1
    
    comparaciones = 0
    
    while numPasados > 0 and intercambios:
        intercambios = False
        
        for i in range(numPasados):
            if lista[i] > lista[i+1]:
                intercambios = True
                
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
            
            comparaciones += 1
            
    numPasados -= 1
        
    return lista, comparaciones
        

lista = [20, 30 , 40, 90 ,50]

lista, comparaciones = ord_burbujeo(lista)
print(lista)
print(f'numeros de comparaciones = {comparaciones}')
