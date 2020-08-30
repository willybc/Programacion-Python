# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:05:58 2020

@author: WILLY
"""
import random

def tirar(tiros):
    tirada = []
    for i in range(tiros):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    cont = 0
    anterior = 0

    for i in tirada:
        if i == anterior:
            cont+=1
        anterior = i

    if cont == 4:
        return True
    else:
        return False

def primer_tirada(tirada):
    cont_rep0 = 0
    cont_rep1 = 0
    cont_rep2 = 0
    cont_rep3 = 0
    cont_rep4 = 0
    for j in tirada:
            if tirada[0] == j:
                cont_rep0+=1
            if tirada[1] == j:
                cont_rep1+=1
            if tirada[2] == j:
                cont_rep2+=1
            if tirada[3] == j:
                cont_rep3+=1
            if tirada[4] == j:
                cont_rep4+=1
    rep = [ cont_rep0, cont_rep1, cont_rep2, cont_rep3, cont_rep4 ]
    cant = max(rep)
    cont=0
    for j in rep :
        if j == cant:
            numero = tirada[cont]    
        cont+=1 
    return numero,cant

tirada = tirar(5)
es_generala(tirada)
numero, cant = primer_tirada(tirada)
print (numero,cant)

def generala_no_servida(tirada):
    numero,cant = primer_tirada(tirada)
    generala = 0
    #0 Falso / 1 True
    if cant == 5 :
        generala = 1
        return generala
    if cant != 5 :
        for i in range(2):
            tirada = tirar(5-cant)
            cant += len([ k for k,j in enumerate(tirada) if j == numero ])
            if cant == 5:
                generala = 1
    
    return generala == 1

N = 1000000
salio_generala_no_servida = [generala_no_servida(tirar(5)) for i in range(N)]
G = sum([generala_no_servida(tirar(5)) for i in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
