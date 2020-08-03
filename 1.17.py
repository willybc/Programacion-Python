cadena = "Ejemplo con for"

contador = 0

for c in cadena:
    print('caracter:',c)
    if c == 'o':
        contador += 1

print(contador)