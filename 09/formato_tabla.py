# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:46:28 2020

@author: wilfr
"""

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        pass
    
    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        pass
    
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))
        
    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        for i in headers:
            print(f'<tr>{i}</tr>', end='')
            #print('<tr>', i, '</tr>', end='')
        print()
        
    def fila(self, data_fila):
        for i in data_fila:
            print(f'<td>{i}</td>', end='')
            #print('<td>', i, '</td>', end='')
        print()
            
def crear_formateador(nombre):
        if nombre == 'txt':
            return FormatoTablaTXT()
        elif nombre == 'csv':
            return FormatoTablaCSV()
        elif nombre == 'html':
            return FormatoTablaHTML()
        else:
            raise RuntimeError(f'Unknow format {nombre}')    