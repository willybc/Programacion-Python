import csv
from collections import Counter

#2.22
#Debe devolver una lista un diccionario con todos los datos por cada arbol del parque elegido
def leer_parque(nombre_archivo, parque):
    fila=[] # lista

    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)    #fila
    headers = next(rows)    #encabezado

    for nrows, rows in enumerate(rows, start=1):
        record = dict(zip(headers, rows))

        if record['espacio_ve'] == parque:
            fila.append(record)
        
    f.close()
    return fila

fila = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
#print(fila)

#2.23
#Tomar lista de arboles y devuelva el conjunto de especies
def especies(lista_arboles):
    rows = lista_arboles
    especies = []
    
    for rows in lista_arboles:
        especies.append(rows['nombre_com'])
        sin_repeticion = set(especies)
    return sin_repeticion

especies = especies(fila)
#print(especies)

#2.24
#Dada una lista , devolver un diccionario en el que las especies sean claves
#y tengan como valores asociados la cantidad de ejemplares en esa
#especie en la lista

def contar_ejemplares(nombre_archivo):
    from collections import Counter
    
    key = [] #lista

    most1= []
    most2= []
    most3= []

    parque1 = 'GENERAL PAZ'
    parque2 = 'ANDES, LOS'
    parque3 = 'CENTENARIO'


    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f) #fila
    headers = next(rows) #encabezado


    tenencias = Counter()
    most1 = Counter()
    most2 = Counter()
    most3 = Counter()

    for nrows, rows in enumerate(rows, start=1):
        record = dict(zip(headers, rows))
        key.append(record['nombre_com'])
        tenencias[record['nombre_com']] += 1

        if record['espacio_ve'] == parque1:
            most1[record['nombre_com']] += 1
        
        if record['espacio_ve'] == parque2:
            most2[record['nombre_com']] += 1

        if record['espacio_ve'] == parque3:
            most3[record['nombre_com']] += 1

    most1 = most1.most_common(5)
    most2 = most2.most_common(5)
    most3 = most3.most_common(5)

    print(f'{parque1:<15} | {parque2:<15} | {parque3:<15}') 
    print(f'{most1[2]} | {most2[2]} | {most3[2]}')
    print(f'{most1[1]} | {most2[1]} | {most2[1]}')
    print(f'{most1[0]} | {most2[0]} | {most1[0]}')
            
    return tenencias

key = contar_ejemplares('../Data/arbolado-en-espacios-verdes.csv')


         