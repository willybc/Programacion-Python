# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:45:04 2020

@author: wilfr
"""

#11.5

def ordenamiento_seleccion(lista):
    n = len(lista) - 1
    contador = 0
    
    while n > 0:
        p, cont = buscar_max(lista, 0, n)
        contador += cont
        
        lista[p], lista[n] = lista[n], lista[p]
        
        n = n - 1
    
    return contador

def buscar_max(lista, ini, fin):
    contador = 0
    pos_max = ini
    for i in range( ini+1, fin+1 ):
        contador += 1
        
        if lista[i] > lista[pos_max]:
            pos_max = i
            
    return pos_max, contador

def ordenamiento_insercion(lista):
    contador = 0
    
    for i in range( len(lista) -1 ):
        
        if lista[i+1] < lista[i]:
            contador += reubicar(lista, i+1)
        
        contador += 1
        
    return contador

def reubicar(lista, p):
    v = lista[p]
    j = p
    contador = 0
    
    while j > 0 and v < lista[ j - 1 ]:
        
        lista[j] = lista[ j -1 ]
        j -= 1
        contador += 1
        
    lista[j] = v
    
    return contador

def ordenamiento_burbujeo(lista):
    intercambios = True
    numPasados = len(lista)-1
    
    contador = 0
    
    while numPasados > 0 and intercambios:
        intercambios = False
        
        for i in range(numPasados):
            if lista[i] > lista[i+1]:
                intercambios = True
                
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
            
            contador += 1
            
    numPasados -= 1
        
    return contador

def merge_sort(lista):
    if len(lista) < 2:
        return lista, 0
    else:
        medio = len(lista) // 2
        izq, count_izq = merge_sort(lista[:medio])
        der, count_der = merge_sort(lista[medio:])
        lista_nueva, comp1 = merge(izq, der)
        
    count = count_der + count_izq + comp1
    
    return lista_nueva, count

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    contador = 0
    
    while(i < len(lista1) and j < len(lista2 )):
        contador += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
            
        else:
            resultado.append(lista2[j])
            j += 1
            
    resultado += lista1[i:]
    resultado += lista2[j:]
    
    return resultado, contador

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]

def comparaciones(N):
    seleccion = np.random.rand(N)
    insercion = np.random.rand(N)
    burbujeo = np.random.rand(N)
    mergesort = np.random.rand(N)
    
    for i in range(1,N+1):
        lista = generar_lista(i)
        seleccion[i-1] = ordenamiento_seleccion(lista[:])
        insercion[i-1] = ordenamiento_insercion(lista[:])
        burbujeo[i-1] = ordenamiento_burbujeo(lista[:])
        mergesort[i-1] = merge_sort(lista[:])[1]
    
    return(seleccion, insercion, burbujeo, mergesort)

x = np.arange(1,257).reshape(-1,1)
xc= x**2
y = comparaciones(256)

lm1 = linear_model.LinearRegression()   
lm1.fit(xc, np.array(y[1]).reshape(-1,1))
lm2 = linear_model.LinearRegression()   
lm2.fit(xc, np.array(y[2]).reshape(-1,1))


plt.plot(x, y[0], c = 'lime', label = 'Selección')
plt.plot(x, lm1.predict(xc), c = 'blue', label = 'Inserción')
plt.plot(x, lm2.predict(xc), c = 'red', label = 'Burbuja', linestyle='dashed')
plt.plot(x, y[3], c = 'orangered', label = 'Merge sort', linestyle='dashed')
plt.title('Comparación de algoritmos de ordenamiento')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Número de comparaciones')
plt.legend()
plt.show()
