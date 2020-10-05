# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:19:50 2020

@author: wilfr
"""
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []
        
    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)
        
    def encolar_prioritario(self, x):
        self.items_con_prioridad.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        elif len(self.items):
            res = self.items.pop(0)
        return res
        
    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items) + len(self.items_con_prioridad)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0
        
class TorreDeControl():
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, vuelo):
         self.arribos.encolar_prioritario(vuelo)
        
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
    
    def ver_estado(self):
        #print('Vuelos esperando para aterrizar:', self.arribos.items_con_prioridad)
        #print('Vuelos esperando para despegar: ', self.partidas.items)    
        #print()
        
        print('Vuelos esperando para aterrizar:\n' + ', '.join(self.arribos.items_con_prioridad), '\n')
        print('Vuelos esperando para despegar:\n'  + ', '.join(self.partidas.items), '\n')
        
    def asignar_pista(self):
        if len(self.arribos.items_con_prioridad) > 0:
            pista_asignada = self.arribos.desencolar()
            return f'El vuelo {pista_asignada} aterrizo con exito'
        
        elif len(self.partidas.items) > 0 :
            pista_asignada = self.partidas.desencolar()
            return f'El vuelo {pista_asignada} aterrizo con exito'
        
        else:
            return 'No existen arribos ni partidas para asignar'
         
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('LAT350')
torre.nuevo_arribo('AR32')
torre.ver_estado()

print(torre.asignar_pista())
print(torre.asignar_pista())
print(torre.asignar_pista())
print(torre.asignar_pista())


