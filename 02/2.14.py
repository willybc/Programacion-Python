import csv
precios = {}

def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r')
    line = csv.reader(f)
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
    
    
leer_precios('../Data/precios.csv')
