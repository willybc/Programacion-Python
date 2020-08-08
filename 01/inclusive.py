frase = 'Todos, tu también'
palabras = frase.split()
nueva_frase = []

for palabra in palabras:
    ultima = len(palabra)-1
    penultima = len(palabra)-2

    if palabra[penultima] == 'o':
        nueva_frase.append( palabra[:penultima] + 'e' + palabra[penultima+1:])

    elif palabra[ultima] == 'o':
        nueva_frase.append( palabra[:ultima] + 'e' + palabra[ultima+1:])
    
    elif palabra[ultima] == ',' and palabra[-3] == 'o':
        nueva_frase.append(palabra[:penultima-1] + 'e' + palabra[penultima:]) 
               
    else:
        nueva_frase.append(palabra)

print(' '.join(nueva_frase))