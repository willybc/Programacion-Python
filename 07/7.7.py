# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:38:53 2020

@author: wilfr
"""

#Ejercicio 7.7 Lectura y seleccion

import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df.head(10)[cols_sel]

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#Ejercicio 7.8 Boxplots

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data=df_lineal_seleccion, hue='nombre_cientifico')