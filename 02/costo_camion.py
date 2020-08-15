#Abrir el archivo que lea las lineas y calcule el precio pagado por los cajones cargados en el camion
#Ayuda para intepretar un string 's' como un numero entero, usa int(s). Para punto flotante , usa float(s)

import csv

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

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
