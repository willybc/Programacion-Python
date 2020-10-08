# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:57:36 2020

@author: wilfr
"""

class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
    #Calculo costo de lote
    def costo(self):
        return self.cajones * self.precio
    
    #Producto vendido 
    def vender(self, x):
        self.cajones -= x
    
