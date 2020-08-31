# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:42:42 2020

@author: WILLY
"""

import random

def envido(primer_baraja):
    palo_anterior = ''
    puntos = 0
    valor_anterior = 0
    primer_valor = 0
    primer_palo = ''
    
    for i in primer_baraja:
        #condicion envido palo anterior
        if i[1] == palo_anterior:
            if valor_anterior == 10 or valor_anterior == 11 or valor_anterior == 12:
                if i[0] == 10 or i[0] == 11 or i[0] == 12:
                    puntos =+ 20
                else:
                    puntos = 20 + i[0]
            
            elif i[0] == 10 or i[0] == 11 or i[0] == 12:
                if valor_anterior == 10 or valor_anterior == 11 or valor_anterior == 12:
                    puntos =+ 20
                else:
                    puntos = 20 + valor_anterior
            else:
                puntos = puntos + 20 + i[0] + valor_anterior
        #condicion envido primero con ultimo
        elif i[1] == primer_palo:
            if primer_valor == 10 or primer_valor == 11 or primer_valor == 12:
                if i[0] == 10 or i[0] == 11 or i[0] == 12:
                    puntos =+ 20
                else:
                    puntos = 20 + i[0]
            
            elif i[0] == 10 or i[0] == 11 or i[0] == 12:
                if primer_valor == 10 or primer_valor == 11 or primer_valor == 12:
                    puntos =+ 20
                else:
                    puntos = 20 + primer_valor
            
            else:
                puntos = puntos + 20 + i[0] + primer_valor
        #guarda los primeros valores de la posicion 0 de la primer_baraja solo 1 vez
        elif palo_anterior == '':
            primer_valor = i[0]
            primer_palo = i[1]
            
        palo_anterior = i[1]
        valor_anterior = i[0]
    return puntos

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

treinta_uno=0
treinta_dos=0
treinta_tres=0

N= 100000
for a in range(0,N):
    primer_baraja = random.sample(naipes, k=3)
    puntaje = envido(primer_baraja)
    
    if puntaje==31:
        treinta_uno+=1
    if puntaje==32:
        treinta_dos+=1
    if puntaje==33:
        treinta_tres+=1
        
print('La probablidad de obtener 31 es de ', treinta_uno/N )
print('La probablidad de obtener 32 es de ', treinta_dos/N )
print('La probablidad de obtener 33 es de ', treinta_tres/N )
