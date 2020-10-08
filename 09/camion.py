# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:21:37 2020

@author: wilfr
"""

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self._lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total