# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:46:55 2020

@author: wilfr
"""
from fileparse import parse_csv
import lote

#8.3
camion_dicts = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion2 = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(sum([i.costo() for i in camion2 ]))