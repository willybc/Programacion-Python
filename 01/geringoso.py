#Usá una iteración sobre el string `cadena` para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:

    if c == 'a':
        capadepenapa += 'apa'
    
    elif c == 'e':
        capadepenapa += 'epe'

    elif c == 'i':
        capadepenapa += 'ipi'

    elif c == 'o':
        capadepenapa += 'opo'

    elif c == 'u':
        capadepenapa += 'upu'
        
    else:
        capadepenapa += c

print(capadepenapa)