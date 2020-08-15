import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')

    reader = csv.reader(f)
    next(reader)

    valores = []
    precio_total = 0.0


    for n_fila, fila  in enumerate(f, start=1):
        try:
            valores = fila.strip().split(",")
            precio_pagado = float(valores[1]) * float(valores[2])
            precio_total = precio_pagado + precio_total
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar:  {valores}' )
    f.close()
    return precio_total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
