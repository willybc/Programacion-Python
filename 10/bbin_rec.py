# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:41:25 2020

@author: wilfr
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e in lista[:medio]:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[medio:], e)
    return res

lista2 = [ 2 , 9 ,3]

a = bbinaria_rec(lista2, 3)
print(a)