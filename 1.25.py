#1.25
##Usá el método  `append()` para agregar `'Mango'` al final de `lista_frutas`.

lista_frutas = ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera']

lista_frutas.append('Mango')

print(lista_frutas)

##Usá el método `insert()` para agregar `'Lima'` como segundo elemento de la lista.

lista_frutas.insert(2, 'Lima')
print(lista_frutas)

##Usá el método `remove()` para borrar `'Mandarina'` de la lista.

lista_frutas.remove('Mandarina')
print(lista_frutas)

##Agregá una segunda copia de `'Banana'` al final de la lista.
#*Observación: es perfectamente válido tener valores duplicados en una lista.*

lista_frutas.append('Banana')
print(lista_frutas)

##Usá el método `index()` para determinar la posición de la primera aparición de `'Banana'` en la lista.
print(lista_frutas.index('Banana'))

##Contá la cantidad de apariciones de `'Banana'` en la lista:
print(lista_frutas.count('Banana'))

#Borrar la primer aparición de 'Banana'
lista_frutas.remove('Banana')
print(lista_frutas)

#1.26
##Ordenar mediante sort()
lista_frutas.sort()
print(lista_frutas)

#Ordenar al revés
lista_frutas.sort(reverse=True)
print(lista_frutas)