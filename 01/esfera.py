#1.13
#Pedir al usuario que ingresa por teclado el radio *r* de una esfera y calcule e imprima el volumen de la misma.
#Recordar que el volúmen de una esfera es 4/3 πr^3*

import math

print('Ingrese el radio de una esfera')
radio = float( input() )

volumen = 4/3 * math.pi * (radio ** 3)

print('Volumen : ', round(volumen,1) )