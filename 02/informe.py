import csv
#Precios pagado al productor de frutas
def leer_camion(nombre_archivo):
    costo_total = 0.0
    fila=[]
    f = open(nombre_archivo, 'rt')
    reader = csv.reader(f)
    encabezados = next(reader)

    for n_fila, fila in enumerate(reader, start=1):
        record = dict(zip(encabezados,fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()   
    return record,costo_total

#Precios de venta
def leer_precios(nombre_archivo):
    precios = {}

    f = open(nombre_archivo, 'r')
    line = csv.reader(f)
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])

    return precios

#Costo camion
camion,costo = leer_camion('../Data/fecha_camion.csv')
#print('Costo camion:', costo)
precios = leer_precios('../Data/precios.csv')

#Recaudacion con la venta
recaudacion=0
recaudacion_total=0

def recau(arch1, arch2):
    fila=[]
    f = open(arch1, 'rt')
    reader = csv.reader(f)
    encabezados = next(reader)
    
    recaudacion = 0
    recaudacion_total = 0

    for n_fila, fila in enumerate(reader, start=1):
        record = dict(zip(encabezados,fila))
        
        ff = open(arch2, 'r')
        line = csv.reader(ff)

        nombre = record['nombre']
        cajones = int(record['cajones'])
        for line in ff:
            row = line.split(',')
            if nombre == row[0]:
                recaudacion = int(cajones) * float(row[1])
                recaudacion_total = (recaudacion_total) + recaudacion    
    f.close()   
    return recaudacion_total

recaudacion_total = recau('../Data/fecha_camion.csv', '../Data/precios.csv')
#print(recaudacion_total)

#Diferencia
diferencia = recaudacion_total - costo
print(f'| Costo camion {costo:<8} | Recaudacion venta {recaudacion_total:<8} | Diferencia {round(diferencia,2):<8}')

if recaudacion_total > costo:
    print('Hubo ganancia!')
elif recaudacion_total == costo:
    print('No ganamos ,ni perdimos')
else:
    print('Perdimos!')