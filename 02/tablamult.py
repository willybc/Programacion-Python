encabezados = ( '0', '1', '2', '3', '4', '5', '6', '7', '8' , '9')
fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('%7s %3s %3s %3s %3s %3s %3s %3s %3s %3s  ' % encabezados)
print('--------------------------------------------')
for i in fila:
    print('%3s %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d' % ('0:',0 , i , i+i, i+i+i, i+i+i+i, i+i+i+i+i, i+i+i+i+i+i, i+i+i+i+i+i+i, i+i+i+i+i+i+i+i, i+i+i+i+i+i+i+i+i) )
