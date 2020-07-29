#Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribir un programa 'rebotes.py' que imprima una tabla mostrando 
#las alturas que alcanza en cada uno de sus primeros diez rebotes.

altura = 100.0
reduccion = 0.6 #3/5
rebotes = 0

while rebotes < 10:
    rebotes = rebotes + 1
    altura = altura * reduccion 
    print('Rebote Nro ', rebotes , ' Altura = ' , round(altura,4) )

#funcion round() : para redondear