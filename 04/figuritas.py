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
             
FIGUS_TOTAL = 670
#album = crear_album(FIGUS_TOTAL)
#print(comprar_figu(FIGUS_TOTAL))
cant = 0
cant = cuantas_figus(FIGUS_TOTAL)