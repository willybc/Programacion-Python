# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:28:00 2020

@author: wilfr
"""
#Ejercicio 7.9 Comparando especies en parques y en verredas

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

#Lectura
directorio = '../Data'
archivo1 = 'arbolado-en-espacios-verdes.csv'
archivo2 = 'arbolado-publico-lineal-2017-2018.csv'

fname1 = os.path.join(directorio, archivo1)
df_parques  = pd.read_csv(fname1)

fname2 = os.path.join(directorio, archivo2)
df_veredas  = pd.read_csv(fname2)

#Nombres cientificos de arboles (CAMBIAR)
nombre_cientifico_parques = 'Tipuana Tipu'
nombre_cientifico_veredas = 'Tipuana tipu'

#Tipos
df_tipos_parques = df_parques[df_parques['nombre_cie'] == nombre_cientifico_parques].copy()
df_tipos_veredas = df_veredas[df_veredas['nombre_cientifico'] == nombre_cientifico_veredas].copy()

#Renombro columnas
df_tipos_parques.rename(columns = {'nombre_com:' : 'nombre', 'altura_tot': 'altura'}, inplace = True)
df_tipos_veredas.rename(columns = {'nombre_cientifico': 'nombre', 'altura_tot' : 'altura', 'diametro_altura_pecho' : 'diametro'}, inplace = True)

#Agrego columna ambiente 
df_tipos_parques['ambiente'] = 'parque'
df_tipos_veredas['ambiente'] = 'vereda'

#Concateno los dos df
df_tipos = pd.concat([df_tipos_parques, df_tipos_parques], sort=False)

#Creo boxplot
sns.boxplot( x = df_tipos['ambiente'], y = df_tipos['altura'])
plt.show()

sns.boxplot( x = df_tipos['ambiente'], y = df_tipos['diametro'])
plt.show()