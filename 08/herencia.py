# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:06:39 2020

@author: wilfr
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones

class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        #Fijate como es el llamado a super().__init__()
        super().__init__(nombre, cajones, precio)
        self.factor = factor
    
    #Remata todos los cajones
    def rematar(self):
        self.vender(self.cajones)
    
    #modifico el costo y le añado un 25% + al costo
    def costo(self):
        return 1.25 * self.cajones * self.precio
    
    def precio(self):
        # Fijate cómo usamos `super`
        costo_orig = super().costo()
        return 1.25 * costo_orig
    
#c = MiLote('Pera', 100, 490.1)
#print(c.precio())