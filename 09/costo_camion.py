# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:36:05 2020

@author: wilfr
"""

import informe

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()