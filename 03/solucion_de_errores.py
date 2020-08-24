#solucion_de_errores.py
#Ejercicios de errores en el código

#Ejercicio 3.1. Función tiene_a()
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#Comentario: El error tipo semantico , esta en la condicion else , ya que si toma cualquier letra que no es 'a' retorna en False 
#    Lo corregí eliminando el else y movimiendo el retorno a false cuando termine el while
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#Comentarios: 
    #Error tipo SyntaxError en la linea 45, esta mal definida la funcion ya que deberia terminar con un ':'
    #Error tipo SyntaxError en la linea 48, esta mal definido el ciclo while ya que deberia terminar con un ':'
    #Error tipo SyntaxError en la linea 49, esta mal definida la condicion if ya que deberia terminar con un ':'
    #Error tipo SyntaxError en la linea 49, esta mal la condicion expresion[i] = 'a' , deberia ser expresion[i] == 'a'  
    #Error tipo NameError en la linea 52, esta retornando a una varible no definida ,
    #segun como esta escrito el codigo doy por hecho que hay que retornar en False
    
    #    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
    
...
...

#%%
#Ejercicio 3.3. Función tiene_uno()
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')
#Comentario: 
    #El error era un typeError y esta ubicado en la linea 95 , al mandarle 1984
    #habria que ponerle comillas , para que lo lea como string
