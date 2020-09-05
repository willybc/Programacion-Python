# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:35:29 2020

@author: WILLY
"""
import csv
#Precios pagado al productor de frutas
def leer_camion(nombre_archivo):
    total = 0.0
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
            total += lote[1] * lote[2] 
    return camion

#Precios de venta
def leer_precios(nombre_archivo):
    precios = {}
    f = open(nombre_archivo, 'r')
    line = csv.reader(f)
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])

    return precios

def hacer_informe(camion, precios):
    tup = ()
    info = {}
    for i in camion:
        nombre = i[0]
        cantidad = i[1]
        precio = i[2]
        for j in precios:
            if j == i[0]:
                precio_venta = (precios[j])
                cambio = precio_venta - precio
                tup = ( nombre , cantidad, precio , cambio)  
                info[i] = tup
    return info

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    lineas = ('----------', '----------', '----------', '----------')
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % lineas)
    
    for x in informe:
        print('%10s %10d     $%.2f %10.2f' % informe[x])
    return

def informe_camion(camion, precios):
    camion = leer_camion(camion)
    precios = leer_precios(precios)
    
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    
    return

informe_camion('../Data/camion.csv', '../Data/precios.csv')
    
