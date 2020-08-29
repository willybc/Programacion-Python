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
    
    for i in tirada:
        if i == anterior:
            cont+=1
        anterior = i
    
    if cont == 4:
        return True
    else:
        return False


tirada = tirar()

respuesta = es_generala(tirada)

#%%
N = 1000000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
