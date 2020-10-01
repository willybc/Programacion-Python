from informe2 import leer_camion
import lote

def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costo = 0
    costo2 = 0.0
    
    #Forma 1 optimizada
    for i in camion:
        costo += i.costo()
    #Forma 2     
    for c in camion:
        costo_fila = c.cajones * c.precio
        costo2 += costo_fila
        
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
