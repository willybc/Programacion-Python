import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    reader = csv.reader(f)
    encabezados = next(reader)
    
    costo_total = 0.0

    for n_fila, fila in enumerate(reader, start=1):
        record = dict(zip(encabezados,fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return costo_total

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)
