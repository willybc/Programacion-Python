from tabla_informe2 import leer_camion

def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costo = 0
    
    for fila in camion:
        costo_fila = fila['cajones'] * fila['precio']
        costo = costo + costo_fila
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
