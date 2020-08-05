frutas = 'Mandarina, Manzana, Pera, Naranja'

print(frutas.lower()) ## transforma todo en minuscula

print(frutas.find('Mandarina')) ## encuentra la posicion de donde se encuentra

print(frutas[13:17]) ## todas las letras que estan entre los intervalos

frutas = frutas.replace('Kiwi','Melón') ## Reemplaza la palabra Kiwi por Melon

nombre = '   Naranja   \n'
nombre = nombre.strip()    # Remueve los espacios en blanco
print(nombre)