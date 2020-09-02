# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:07:08 2020

@author: WILLY
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_parque(nombre_archivo, parque):
    fila=[] # lista
    
    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)    #fila
    headers = next(rows)    #encabezado

    for nrows, rows in enumerate(rows, start=1):
        record = dict(zip(headers, rows))

        if record['espacio_ve'] == parque:
            fila.append(record)
        
    f.close()
    return fila

def medidas_de_especies(especies,arboleda):
    elementos = len(especies)
    record2 = {}
    
    for i in range(0,elementos):
        
        H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especies[i]] 
        D = [round(float(arbol['diametro']) * 0.1, 2) for arbol in arboleda if arbol['nombre_com'] == especies[i]]
        
        dict1 = dict(zip(H, D))
        
        record = { especies[i]: dict1 for arbol in arboleda }        
        record2.update(record)
  
    return record2
    
arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

#Lista de alturas
H=[float(arbol['altura_tot']) for arbol in arboleda]

H_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
D_jacaranda = [round(float(arbol['diametro']) * 0.1, 2) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
tupla = list(zip(H_jacaranda, D_jacaranda))

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
diccionario = medidas_de_especies(especies,arboleda)
print(diccionario)

#4.30
#plt.hist(H_jacaranda,bins=20)

#4.31
d = np.array(H_jacaranda)
h = np.array(D_jacaranda)

color=("green")


plt.scatter(d, h, alpha=0.8, c=color, edgecolors='none', s=30)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Jaranda")
plt.show()




