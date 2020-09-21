# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 03:09:54 2020

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

def maximo(lista):
    m = -99999
    for e in lista:
        if e > m:
            m = e
    
    return m

def donde_insertar(lista, x):
    #Realizo la busqueda binaria
    pos = -1 # valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos != -1:
        return pos
    else:
        for i in lista:
            if (x > i) and (lista.index(i)<len(lista)-1):
                pass
            else:
                if (x > i) and (lista.index(i) == len(lista)-1) :
                    return (lista.index(i)+1)
                else:
                    return lista.index(i)
                
def insertar(lista, x):
    #Realizo la busqueda binaria
    pos = -1 # valor no encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos != -1:
        return pos
    else:
        for i in lista:
            if (x > i) and (lista.index(i)<len(lista)-1):
                pass
            else:
                if (lista.index(i) == len(lista)-1) and (x > i):
                    lista.insert(lista.index(i)+1,x)
                    return ((lista.index(x)),lista)
                else:
                    lista.insert(lista.index(i),x)
                    return (lista.index(x),lista)

lista = [1,2,3,2,3,4]
buscar_u_elemento(lista, 5)
buscar_n_elemento(lista, 2)

max = maximo([-5,-4])

a = donde_insertar([0,2,4,6], 3)
b = insertar([0,2,4,6], 6)