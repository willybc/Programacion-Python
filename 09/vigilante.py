# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:01:45 2020

@author: wilfr
"""

# vigilante.py
import os
import time

def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
            
            
            
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    naranjas = filematch(lines, 'Naranja')
    for line in naranjas:
        print(line)
        
'''  
    import informe
    camion = informe.leer_camion('../Data/camion.csv')
    
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
'''     
