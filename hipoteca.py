# hipoteca.py
##Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca
##Modificar el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

pago_extra = 1000
duracion_extra = 12

contador_mes = 0

while saldo >= 0:
    saldo = (saldo * (1+tasa/12) ) - pago_mensual

    if duracion_extra > 0:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
        duracion_extra = duracion_extra -1
        
    total_pagado = total_pagado + pago_mensual

    contador_mes= contador_mes + 1

print('Total pagado', round(total_pagado, 2), 'en', contador_mes, 'meses.')

