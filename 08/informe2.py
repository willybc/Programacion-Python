# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:35:29 2020

@author: WILLY
"""
import lote
from fileparse import parse_csv
#Precios pagado al productor de frutas
def leer_camion(nombre_archivo):
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types=[str, int,float])
    camion2 = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion]
    return camion2

#Precios de venta
def leer_precios(nombre_archivo):
    precios = parse_csv(nombre_archivo, types=[str,float], has_headers=False)
    return precios

def hacer_informe(camion,precios):
    tup = ()
    info = []
    
    pago_prod = 0.0
    valor_mercado = 0.0
    venta_total = 0.0
    
    for i in camion:
        nombre = i.nombre
        cantidad = i.cajones
        precio = i.precio
    
        pago_prod += i.cajones * i.precio
		#valor_mercado += precios[i['nombre']]*i['cajones']
        
        for j in precios:
            if j[0] == i.nombre:
                precio_venta = (j[1])
                venta_total += i.cajones* precio_venta
                cambio = precio_venta - precio
                tup = ( nombre , cantidad, precio , cambio)  
                info.append(tuple(tup))
    
    print('Costo de productos', pago_prod)
    print(f'Total de venta {venta_total}')
    balance = venta_total - pago_prod
    if balance > 0:
        print('Hubo ganancia y fue de : ', round(balance, 2), '\n\n' )
    else:
        print('No hubo ganancia \n\n')
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


