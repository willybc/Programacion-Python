# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 01:30:53 2020

@author: wilfr
"""

import random
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt

def ordenamiento_seleccion(lista):
    n = len(lista) - 1    
    while n > 0:
        p = buscar_max(lista, 0, n)        
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    
    return

def buscar_max(lista, ini, fin):
    pos_max = ini
    for i in range( ini+1, fin+1 ):
        if lista[i] > lista[pos_max]:
            pos_max = i
            
    return pos_max

def ordenamiento_insercion(lista):
    
    for i in range( len(lista) -1 ):
        
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
        
    return 

def reubicar(lista, p):
    v = lista[p]
    j = p    
    while j > 0 and v < lista[ j - 1 ]:
        
        lista[j] = lista[ j -1 ]
        j -= 1
        
    lista[j] = v
    return

def ordenamiento_burbujeo(lista):
    intercambios = True
    numPasados = len(lista)-1
    
    while numPasados > 0 and intercambios:
        intercambios = False
        
        for i in range(numPasados):
            if lista[i] > lista[i+1]:
                intercambios = True
                
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    numPasados -= 1 
    return

def merge_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]

def experimento(listas, num):
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []
    
    global lista 
    
    for lista in listas :
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ordenamiento_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ordenamiento_insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('ordenamiento_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)
        
    #paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)
    
    return np.array([tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge])

listas = []
for N in range(1, 257):
    listas.append(generar_lista(N))

tiempos_orden = experimento(listas, 10)

plt.plot(tiempos_orden[0], label = 'Selección')
plt.plot(tiempos_orden[1], label = 'Inserción')
plt.plot(tiempos_orden[2], label = 'Burbujeo')
plt.plot(tiempos_orden[3], label = 'Merge sort')
plt.title('Comparación de tiempos de ejecución')
plt.ylabel('Tiempo (s)')
plt.xlabel('Largo de la cadena')
plt.legend()
plt.show()