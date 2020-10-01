# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:46:42 2020

@author: wilfr
"""

#8.1
import lote
print('\n\n')

a = lote.Lote('Pera', 100, 490.10)
b = lote.Lote('Manzana', 50, 122.34)
c = lote.Lote('Naranja', 75, 91.75)

lotes = [a, b, c]

for i in lotes:
    print(f'{i.nombre:>10s} {i.cajones:>10d} {i.precio:>10.2f}')