# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:05:58 2020

@author: WILLY
"""
import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    cont = 0
    anterior = 0
    lista = []

    
    for i in tirada:
        if i == anterior:
            cont+=1
            lista.append(i)
        else:
            lista.append(i)
        anterior = i
    print('tiradas', lista)
    return lista
    '''    
    if cont == 4:
        return True
    else:
        return False
    '''

def primer_tirada(lista):
    cont_rep0 = 0
    cont_rep1 = 0
    cont_rep2 = 0
    cont_rep3 = 0
    cont_rep4 = 0
    for j in lista:
            if lista[0] == j:
                cont_rep0+=1
            if lista[1] == j:
                cont_rep1+=1
            if lista[2] == j:
                cont_rep2+=1
            if lista[3] == j:
                cont_rep3+=1
            if lista[4] == j:
                cont_rep4+=1
    rep = [ cont_rep0, cont_rep1, cont_rep2, cont_rep3, cont_rep4 ]
    #print('posicio',rep)
    a = max(rep)
    cont3=0
    for j in rep :
        if j == a:
            valor = lista[cont3]    
        cont3+=1

    print('numero ',valor)
    print('aparecio', a, 'veces')
    
    return valor,a

tirada = tirar()
lista = es_generala(tirada)

valor, a = primer_tirada(lista)

N = 1000000
#salio_generala_servida = [es_generala(tirar()) for i in range(N)]
#G = sum([es_generala(tirar()) for i in range(N)])
#prob = G/N

#print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
#print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')