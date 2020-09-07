# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:35:29 2020

@author: WILLY
"""
from fileparse import parse_csv
#Precios pagado al productor de frutas
def leer_camion(nombre_archivo):
    camion = parse_csv(nombre_archivo,types=[str, int,float])
    return camion

#Precios de venta
def leer_precios(nombre_archivo):
    precios = parse_csv(nombre_archivo, types=[str,float], has_headers=False)
    return precios

def hacer_informe(camion,precios):
    tup = ()
    info = []
    for i in camion:
        nombre = i['nombre']
        cantidad = i['cajones']
        precio = i['precio']
        for j in precios:
            if j[0] == i['nombre']:
                precio_venta = (j[1])
                cambio = precio_venta - precio
                tup = ( nombre , cantidad, precio , cambio)  
                info.append(tuple(tup))

    return info

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    lineas = ('----------', '----------', '----------', '----------')
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % lineas)
    
    for x in informe:
        valores = (x[0] , x[1], x[2], x[3])
        print('%10s %10d     $%.2f     $%.2f' % valores)
    return

def informe_camion(ubi_camion, ubi_precios):
    camion = leer_camion(ubi_camion)
    precios = leer_precios(ubi_precios)
    
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    
    return

informe_camion('../Data/camion.csv', '../Data/precios.csv')
    
