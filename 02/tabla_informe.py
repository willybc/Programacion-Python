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

#print('Costo camion:', costo)
precios = leer_precios('../Data/precios.csv')

#Recaudacion con la venta
recaudacion=0
recaudacion_total=0


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


camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

informe = hacer_informe(camion, precios)

for x in informe:
    print(informe[x])
