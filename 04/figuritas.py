# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 02:57:07 2020

@author: WILLY
"""
#1. Álbum con 670 figuritas.
#2. Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#3. Cada paquete trae cinco figuritas.

import random 
import numpy as np



def crear_album(figus_total):
    album = np.zeros(figus_total).astype(int)
    return album
                
def album_incompleto(album):
    if album.all() == 0:
        return True
    else:
        return False
        
def comprar_figu(figus_total):
    figurita = random.randint(0,figus_total-1)
    return figurita
   
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cantidad_figuritas = 0
    
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1
        cantidad_figuritas += 1
    
    return cantidad_figuritas

def armado_paquete(figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        figuritas = random.randint(0,figus_total-1)
        paquete.append(figuritas)
    return paquete

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    cantidad_figuritas = 0
    
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = armado_paquete(figus_paquete)
        for i in paquete:
            #condicion para no olvidar de contar las figuritas repetidas
            if album[i] == 1:
                cantidad_figuritas += 1
            else:
                album[i] +=1
                cantidad_figuritas += 1
    
    paquetes_comprados = cantidad_figuritas / figus_paquete
    return paquetes_comprados
                            
    
#album = crear_album(figus_total)
#print(comprar_figu(figus_total))


'''
#4.19
cant = 0
figus_total = 6
n_repeticiones = 1000
cant = [ cuantas_figus(figus_total) for i in range(n_repeticiones) ]
promedio = np.mean(cant)

#4.20
figus_total = 670
n_repeticiones = 100
cant = [ cuantas_figus(figus_total) for i in range(n_repeticiones) ]
promedio = np.mean(cant)
#print(promedio)

#4.23
figus_total = 670
figus_paquete = 5
paquetetes_comprados = comprar_paquete(figus_total, figus_paquete)

'''
#4.24
n_repeticiones = 1000
figus_total = 670
figus_paquete = 5

cant = [ (comprar_paquete(figus_total, figus_paquete) ) for i in range(n_repeticiones) ]
promedio = sum(cant)/len(cant)
#958.624




