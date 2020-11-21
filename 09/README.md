# 9. Generadores e iteradores
Programar es básicamente escribir condicionales, ciclos y asignaciones de variables. Aunque no de cualquier forma.

Los ciclos, ya sean ciclos `while` o iteraciones `for` son una de las estructuras más ubicuas en cualquier lenguaje. Los programas hacen muchas iteraciones para procesar listas, leer archivos, buscar en bases de datos y demás. 

Una de las características más poderosas de Python es la capacidad de redefinir la iteración mediante las llamadas "funciones generadoras". En esta sección veremos de que se trata ésto. Hacia el final vas a escribir programas que procesan datos en tiempo real, a medida que son generados. 

Terminamos la clase con un ejercicio optativo que combina dos temas importantes: objetos y simulaciones. El ejercicio optativo propone simular en el espacio y tiempo la dinámica predador-presa utilizando para esto programación orientada a objetos.

* [9.1 El protocolo de iteración](01_protocolo_Iteracion.md)
* [9.2 Iteración a medida](02_iteracion_a_medida.md)
* [9.3 Productores, consumidores y cañerías.](03_Producers_consumers.md)
* [9.4 Más sobre generadores](04_Mas_generadores.md)
* [9.5 Predador Presa](05_PredadorPresa.md)
* [9.6 Cierre de la novena clase](06_Cierre.md)

# Cierre de clase

En esta clase aprendiste sobre generadores e iteradores, dos conceptos muy interesantes de Python. Viste que el mecanismo de iteración es una forma de dialogar con un objeto. Además, aprendiste los métodos que necesitás implementar para que un objeto que creaste sea iterable. 

Discutimos también las ventajas de construír un programa con estos conceptos. Los programas resultan mas versátiles, modulares, y ligeros. Como con el concepto de comprensión de listas, podés usar la sintaxis de comprensión para construír un iterable: una expresión sobre la cual podés iterar sin necesidad de almacenar todos los elementos posibles en una lista ni escribir una función para calcularlos.

Por último, viste la ventaja de crear pipelines: estructuras de procesamiento de datos configurables en vuelo, altamente modulares.  

Aunque no la uses de inmediato, cuando te la apropies, esta arquitectura puede cambiarte (un poquito) la vida.

Para cerrar esta clase, prepará:
 
* El archivo `informe.py` del [Ejercicio 9.2](../09_Generadores_e_Iteradores/01_protocolo_Iteracion.md#ejercicio-92-iteración-sobre-objetos).
* El archivo `camion.py` del [Ejercicio 9.3](../09_Generadores_e_Iteradores/01_protocolo_Iteracion.md#ejercicio-93-un-iterador-adecuado) (o [Ejercicio 9.14](../09_Generadores_e_Iteradores/04_Mas_generadores.md#ejercicio-914-expresiones-generadoras-como-argumentos-en-funciones)) que va a jugar en la revisión de pares.
* El archivo `vigilante.py` del [Ejercicio 9.7](../09_Generadores_e_Iteradores/02_iteracion_a_medida.md#ejercicio-97-cambios-de-precio-de-un-camión).
* El archivo `ticker.py` del [Ejercicio 9.12](../09_Generadores_e_Iteradores/03_Producers_consumers.md#ejercicio-912-el-pipeline-ensamblado) (o del [Ejercicio 9.15](../09_Generadores_e_Iteradores/04_Mas_generadores.md#ejercicio-915-código-simple)).
* Y, opcionalmente, el archivo `simulacion.py` del [Ejercicio 9.19](../09_Generadores_e_Iteradores/05_PredadorPresa.md#ejercicio-919-alcanzando-la-madurez).
