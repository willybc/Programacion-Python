# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:16:15 2020

@author: wilfr
"""

import informe

camion = informe.leer_camion('../Data/camion.csv')

print(len(camion))

print(camion[0])
print(camion[1])
print(camion[0:3])

print('Naranja' in camion)

print('Manzana' in camion)