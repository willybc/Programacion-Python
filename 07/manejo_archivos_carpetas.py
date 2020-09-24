# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:39:51 2020

@author: WILLY
"""
#%% Obtener directorio actual
import os
a = os.getcwd()
print(a)
#%% Cambiar el directorio de trabajo
os.chdir('../Data')     #entro en Data
print(os.getcwd())

os.chdir('..')          #voy para atras
print(os.getcwd())

#%% Para cambiar de directorio, como cadena
#directorio = os.path.join('C:\\', 'Users', 'WILLY')
#os.chdir(directorio)

#Listar directorios y archivos
c = os.getcwd()
print(c)

d = os.listdir('07')
print(d)

#%% Crear directorio
os.mkdir('test') #crear directorio test
os.mkdir(os.path.join('test', 'carpeta')) #creo el subdirectorio carpeta dentro de test
e = os.listdir('test')
print(e)

#%% Renombrar un directorio o un archivo
os.chdir('test')
os.listdir()
#['carpeta']
os.rename('carpeta', 'carpeta_nueva')
os.listdir()
#['carpeta_nueva']

#%% Recorriendo dictorios con os.walk()
import os
for root, dirs,files in os.walk("."):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))    
        
#%% Cambiar atributos de un archivo
import os
import datetime
import time
a = os.getcwd()
print(a)
camino = '../Data/01/rebotes.py'
stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))