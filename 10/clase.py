# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 00:29:34 2020

@author: wilfr
"""

#Sumar modo recursivo
def sumar(a, b):
    print(f"LLame a sumar {a} {b}")
    if b == 0:
        res = a
    else:
        res = 1 + sumar(a, b-1)
    
    return res

#Factorial
def factorial(n):
    if n == 1:
        res = 1
    else:
        res = n * factorial(n-1)
    
    return res

def es_impar(n, str_tab=""):
    if n == 0:
        print(f"{str_tab} llegue al cero")
        res = False
    else:
        print(f"{str_tab} para saber si {n} es impar, niego la paridad de uno menos")
        temp = es_impar(n-1, str_tab + "\t")
        res = not temp
        print(f"{str_tab} para saber si {n} obtuve es_impar({n-1})={temp} y lo negue para obtener {res}")
        
    return res

def maximo(lista, debug_extra_str=""):
    
    print(f"{debug_extra_str}Acabo de entrar con {lista}")
    if len(lista) == 1:
        res = lista[0]
        print(f"{debug_extra_str}En el caso base")
    else:
        primero = lista[0]
        max_del_resto = maximo(lista[1:], debug_extra_str+"\t")
        res = max(primero, max_del_resto)
        print(f"{debug_extra_str}Asigno res=max({primero}, maximo ({lista[1:]}))=max({primero}, {max_del_resto})={res}")
    
    print(f"{debug_extra_str}Devuelvo: {res}")
    return res

def permutaciones(lista):
    
    if len(lista) == 0:
        res = []
        
    elif len(lista) == 1:
        res = [lista]
    
    else:
        res = []
        for idx, elem in enumerate(lista):
            permut_resto = permutaciones(lista[:idx] + lista[idx+1:])
            res += [ [elem] + p for p in permut_resto ]
    
    return res
