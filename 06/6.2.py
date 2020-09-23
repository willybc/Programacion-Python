# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 01:34:31 2020

@author: WILLY
"""

from fileparse import parse_csv
import gzip

with open('missing.csv') as f:
    camion_1 = parse_csv(f,select=['nombre', 'cajones'], types = [str, int, float],silence_errors = False)

print(camion_1)

#%%
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion_2 = parse_csv(lines, types=[str,int,float])
print(camion_2)

#%%
camion_3 = parse_csv('camion.csv', types=[str,int,float])
print(camion_3) 