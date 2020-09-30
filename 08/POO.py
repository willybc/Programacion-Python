# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:38:56 2020

@author: wilfr
"""

nums = [1, 2, 3]
nums.append(4)
nums.insert(1, 10)


#Instruccion de Jugador
class Jugador:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.salud = 100
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def lastimar(self, pts):
        self.salud -= pts

#Instancias
a = Jugador(2, 3)
b = Jugador(10, 20)

a.mover(1, 2)
