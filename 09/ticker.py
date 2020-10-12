# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:30:28 2020

@author: wilfr
"""

#ticker.py

from vigilante import vigilar
import csv

def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

#9.11
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

import informe
camion = informe.leer_camion('../Data/camion.csv')
filas = parsear_datos(vigilar('../Data/mercadolog.csv'))
filas = filtrar_datos (filas, camion)
for fila in filas:
    print(fila)


'''
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)'''
        
