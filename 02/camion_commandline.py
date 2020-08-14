import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    reader = csv.reader(f)
    next(reader)
    
    valores = []
    precio_total = 0.0

    for line in f:
        try:
            valores = line.strip().split(",")
            precio_pagado = float(valores[1]) * float(valores[2])
            precio_total = precio_pagado + precio_total
        except ValueError:
           print(f'error en lectura de datos en fila {line}' )
    f.close()
    return precio_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
