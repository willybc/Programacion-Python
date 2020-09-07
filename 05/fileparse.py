# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:30:07 2020

@author: WILLY
"""

import csv
'''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
'''

def parse_csv(nombre_archivo, select=['nombre', 'cajones'], types=[str, int], has_headers=True):

    with open(nombre_archivo) as f:
        
        if has_headers == False:
            registros = {}
            
            filas = csv.reader(f)
            for fila in f:
                row = fila.split(',')
                registros[row[0]] = float(row[1])
            
        else:
            # Lee los encabezados del archivo
            filas = csv.reader(f)
            encabezados = next(filas)
            
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios            
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]

                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv', types=[str, int, float])
precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)