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

#fila = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
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

#key = contar_ejemplares('../Data/arbolado-en-espacios-verdes.csv')

def obtener_alturas(lista_arboles, especie):
    rows = lista_arboles
    alturas = []
    alturas2 = []

    for rows in lista_arboles:
        columna = rows['nombre_com']
        altura = float((rows['altura_tot']))
        lugar = rows['espacio_ve']
        #lista 'alturas' = [columna , altura]
        filas = (columna, altura)
        alturas.append(filas) 

        #lista 'alturas2' = [columna , altura, lugar]
        filas2 = (columna, altura, lugar)
        alturas2.append(filas2)

    return alturas,alturas2

fila1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
fila2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
fila3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

alturas_general, alturas_general2 = obtener_alturas(fila1, especies)
alturas_andes, alturas_andes2 = obtener_alturas(fila2, especies)
alturas_cente, alturas_cente2 = obtener_alturas(fila3, especies)

parque1 = 'GENERAL PAZ'
parque2 = 'ANDES, LOS'
parque3 = 'CENTENARIO'

max1=0.0
max2=0.0
max3=0.0

prom1=0.0
prom2=0.0
prom3=0.0

cont1=0
cont2=0
cont3=0

sum1=0
sum2=0
sum3=0

for x in alturas_general2:
    if x[2] == parque1:
        if x[0] == 'Jacarandá':
            cont1+=1
            sum1+=x[1]
            if max1 < x[1]:
                max1 = x[1]

prom1 = sum1/cont1

for y in alturas_andes2:
    if y[2] == parque2:
        if y[0] == 'Jacarandá':
            #print(y)
            cont2+=1
            sum2+=y[1]
            if max2 < y[1]:
                max2 = y[1]

prom2 = sum2/cont2

for w in alturas_cente2:
    if w[2] == parque3:
        if w[0] == 'Jacarandá':            
            cont3+=1
            sum3+=w[1]
            if max3 < w[1]:
                max3 = w[1]    

prom3 = sum3/cont3

print('Med\t\tGeneral Paz\t\tLos Andes\t\tCentenario') 
print('Alt\t\t',max1,'\t\t\t',max2,'\t\t\t',max3)
print('Pro\t\t',round(prom1,2),'\t\t\t',round(prom2,2),'\t\t\t',round(prom3,2))

def obtener_inclinaciones(lista_arboles, especies):
    rows = lista_arboles
    inclinaciones = []

    for rows in lista_arboles:
        columna = rows['nombre_com']
        inclinacion = rows['inclinacio']

        filas = (columna, inclinacion)
        inclinaciones.append(filas)
    return inclinaciones

fila = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
inclinaciones = obtener_inclinaciones(fila,especies)
#print(inclinaciones)


def especimen_mas_inclinado(lista_arboles):
    rows = lista_arboles
    max_inclinacion=0
    especie_max={''}
    
    #devuelve el espacio
    espacio={''}
    for d in rows:
        espacio = d['espacio_ve']

    for rows in lista_arboles:
        columna = rows['nombre_com']
        inclinacion = int(rows['inclinacio'])
        
        if int(inclinacion) > max_inclinacion:
            max_inclinacion = inclinacion
            especie_max = columna
    return max_inclinacion, especie_max, espacio

fila1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
fila2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
fila3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

max_inclinacion, especie_max, espacio = especimen_mas_inclinado(fila1)
print(f'En el parque {espacio} hay un {especie_max} inclinado {max_inclinacion} grados')

max_inclinacion, especie_max, espacio = especimen_mas_inclinado(fila2)
print(f'En el parque {espacio} hay un {especie_max} inclinado {max_inclinacion} grados')

max_inclinacion, especie_max, espacio = especimen_mas_inclinado(fila3)
print(f'En el parque {espacio} hay un {especie_max} inclinado {max_inclinacion} grados')

    