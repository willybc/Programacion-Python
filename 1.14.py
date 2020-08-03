#Agrega 'Melón'` al principio de la cadena:

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas = frutas + ',' + 'Pera'

frutas = 'Melón' + ',' + frutas 

print(frutas)

#>>> 'Naranja' in frutas
#True
#>>> 'nana' in frutas
#True
#>>> 'Lima' in frutas
#False
#>>>

#*¿Por qué la verificación de `'nana'` dió `True`?*
#Porque nana es parte del string , Banana