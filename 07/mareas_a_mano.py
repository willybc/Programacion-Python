# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 03:49:18 2020

@author: wilfr
"""
#Lectura de archivos temporales
import pandas as pd

#Uso la columna 'Time' como índice (index_col = ['Time']) 
#La interprete como un timestamp (parse_dates = True)
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#Ejercicio 7.10
dh = df['12-25-2014':].copy()

delta_t = -1 #tiempo que tarda la marea entre ambos puertos
delta_h = 17 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()


