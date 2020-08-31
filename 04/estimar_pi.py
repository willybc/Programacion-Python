# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:51:55 2020

@author: WILLY
"""
import random 


def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


N = 100000
M = sum([(x ** 2 + y ** 2) < 1 for x, y in [generar_punto() for i in range(N)]])

pi = 4*M/N  
print('Pi =', pi)     
        