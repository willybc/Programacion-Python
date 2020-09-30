# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:46:06 2020

@author: wilfr
"""

#%% Lectura de datos
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

#df.head() Para ver las primeras lineas

#%% Caminatas al azar
import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

