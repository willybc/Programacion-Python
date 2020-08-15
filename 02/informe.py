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
    return camion,total

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
camion,costo = leer_camion('../Data/camion.csv')
#print('Costo camion:', costo)

precios = leer_precios('../Data/precios.csv')

#Recaudacion con la venta
recaudacion=0
recaudacion_total=0
for i in camion:
    for n in precios:
        if n == i[0]:
            recaudacion = precios[n] * i[1]
            recaudacion_total = recaudacion_total + recaudacion
#print('Recaudacion total:', round(recaudacion_total,2))

#Diferencia
diferencia = recaudacion_total - costo
#print('Diferencia:', round(diferencia,2))

print(f'| Costo camion {costo:<8} | Recaudacion venta {recaudacion_total:<8} | Diferencia {round(diferencia,2):<8}')

if recaudacion_total > costo:
    print('Hubo ganancia!')
elif recaudacion_total == costo:
    print('No ganamos ,ni perdimos')
else:
    print('Perdimos!')
    



    
    