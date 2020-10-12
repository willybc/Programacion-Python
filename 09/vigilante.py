# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:01:45 2020

@author: wilfr
"""

# vigilante.py
import os
import time

f = open('../Data/mercadolog.csv')
f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el 

def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line
                

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Esperar un rato y
        continue          # vuelve al comienzo del while
    fields = line.split(',')
    nombre = fields[0].strip('"')
    precio = float(fields[1])
    volumen = int(fields[2])
    if volumen > 1000:
        print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')