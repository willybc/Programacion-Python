# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:06:18 2020

@author: WILLY
"""

#Escribir un programa que dado un directorio,
#imprimir en la pantalla los nombres de todos los archivos png

#Debera de poder ejecutarse desde la linea de comandos

#Guardar resultando en archivo listar_imgs.py
import os
import sys

#a = os.getcwd()
#os.chdir('../Data')
#print(os.getcwd()) Estoy parado en Data

directorio = str(sys.argv[1])

'''
py (ruta de programa) (ruta de directorio)
Muestra los archivos .png de la ruta del directorio dada
'''


def listar_imgs(directorio):
    imgs = []
    
    for root, dirs,files in os.walk(directorio):
        for name in files:
            if (name.endswith('.png')):
                imgs.append(os.path.join(root, name))
                print(os.path.join(root, name))
    
    if len(imgs) == 0:
        print('No hay imagenes en tu directorio')
        
    return imgs

if __name__ == '__main__':
    listar_imgs(sys.argv[1])