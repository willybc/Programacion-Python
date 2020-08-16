import csv
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

#Tome lista de arboles y devuelva el conjunto de especies
#columna 'nombre_com'

#Sugerencia : Usar comando set
import csv
def especies(lista_arboles):
    rows = lista_arboles
    especies = []
    
    for rows in lista_arboles:
        especies.append(rows['nombre_com'])
        sin_repeticion = set(especies)
    return sin_repeticion

especies = especies(fila)
print(especies)