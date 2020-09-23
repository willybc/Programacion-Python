# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:12:07 2020

@author: WILLY
"""
from datetime import datetime
from datetime import timedelta

#Contando todos los dias para adelante
inicio = datetime(2020,9,26)
duracion = inicio + timedelta(days=200)
print('La licencia terminara en :', duracion)
