# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:27:35 2020

@author: wilfr
"""

from vigilante import vigilar
import csv

lineas = vigilar('../Data/mercadolog.csv')
filas = csv.reader(lineas)
for fila in filas:
    print(fila)