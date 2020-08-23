# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:07:08 2020

@author: WILLY
"""
import csv

def leer_parque(nombre_archivo, parque):
    fila=[] # lista

    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)    #fila
    headers = next(rows)    #encabezado

    for nrows, rows in enumerate(rows, start=1):
        record = dict(zip(headers, rows))

        if record['espacio_ve'] == parque:
            fila.append(record)
        
    f.close()
    return fila

arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

#Lista de alturas

H=[float(arbol['altura_tot']) for arbol in arboleda]
H_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
