# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:38:05 2020

@author: wilfr
"""
#n fila
#k columna
def pascal(n, k):
    
    if n == 0 and k == 0:
        return 1
    
    if n < 0 or k < 0:
        return 0
    
    else:
        return pascal(n - 1, k) + pascal(n-1, k-1)
    
print(pascal(5,2))