# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:10:13 2020

@author: wilfr
"""

import costo_camion
import informe

costo_camion.costo_camion('../Data/camion.csv')
informe.informe_camion('../Data/camion.csv', '../Data/precios.csv')