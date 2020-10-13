# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:25:26 2020

@author: wilfr
"""

#%%9.13
nums = [1, 2, 3, 4, 5]
cuadrados = ( x*x for x in nums )

for n in cuadrados:
    print(n)
    
#%% 9.14
nums = [1, 2, 3, 4, 5]
a = sum([ x*x for x in nums ])       #una lista por compresion
b = sum( x*x for x in nums )        #una expresion generadora