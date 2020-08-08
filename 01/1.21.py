texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020'

import re

#Encuentra las aparaciones de una fecha en el texto
print(re.findall(r'\d+/\d+/\d+', texto)) 
#['6/8/2020', '7/8/2020']


#Reemplaza las aparaciones, cambiando el formato
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))
#Hoy es 2020-8-6. Mañana será 2020-8-7

#Para mas información sobre el módulo `re`, mirá la [documentación oficial en inglés](https://docs.python.org/3/library/re.html) o algún [tutorial en castellano](https://rico-schmidt.name/pymotw-3/re/index.html).