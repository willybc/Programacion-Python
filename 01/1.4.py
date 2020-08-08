#El siguiente fragmento de código está relacionado con el problema del obelisco. Tiene un bug, es decir, un error.

grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete < altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    dia = dia + 1
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)

# ¿En qué linea está el error? linea #10

# ¿Cuál es el error? El contador estaba sumando a una variable erronea y vacia

# Repará el error.
# Ejecutá el programa exitosamente.