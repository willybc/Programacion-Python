# 6. Diseño, especificación, documentación y estilo.
En este curso queremos que aprendas a escribir un script que te resuelva un problema computacional. Pero también queremos que puedas escribir adecuadamente programas más grandes, que los puedas compartir y volver a usar vos misme unos años más tarde.

Por eso insistimos con algunos temas de estilo, documentación, especificiación y diseño que ya hemos comentado anteriormente y sobre los que volveremos en esta clase. Uno de ellos es que es conveniente administrar los errores; seguiremos hablando sobre las formas adecuadas de hacerlo y porqué no conviene hacerlo de más. También se vuelve indispensable estructurar adecuadamente el código y aprender a definir una función *main*. Vamos a continuar con nuestras discusiones sobre el diseño de algoritmos y sus estructuras de datos asociadas. También queremos que aprendas algunos conceptos elementales sobre especificación de problemas. Son procesos de abstracción que nos ayudan a pensar con mayor claridad. Al especificar un problema con precondiciones y poscondiciones estamos definiendo qué es lo que debe pasar en una función, por ejemplo (aunque en ningún momento decimos cómo debe pasar esto). Una especificación es como un contrato y podemos definir varias funciones que cumplan el contrato, y cada una puede resolverlo a su manera.

Finalmente, daremos un poco más sistemáticamente algunos conceptos de la biblioteca `matplotlib`, incluyendo el manejo de figuras y subplots.
* [6.1 Control de errores]
* [6.2 El módulo principal]
* [6.3 Cuestiones de diseño]
* [6.4 Contratos: Especificación y Documentación]
* [6.5 Estilos de codeo]
* [6.6 La biblioteca matplotlib]
* [6.7 Cierre de la sexta clase]

# Cierre de la sexta clase

En esta sexta clase vimos cómo se hace una administración eficiente de errores, cómo atrapar excepciones, cómo lanzarlas, y cuándo conviene hacer o no hacer estas cosas.

Vimos que un archivo `.py` correctamente escrito puede usarse como un módulo, como un programa en sí mismo, o como ambas cosas dependiendo del caso, y mostramos que aunque uno esté escribiendo una pequeña función para solucionar un pequeño problema, es bueno pensar en grande y no imponer restricciones innecesarias.

Aprendimos a documentar y comentar de manera útil, y mostramos el paradigma de contratos. Además vimos algo sobre estilo código estándard.

También estudiamos diversos estilos de gráficos, como obtener un vistazo rápido de los datos y como ajustar cada elemento para obtener un gráfico que pueda ser publicado.

Para cerrar esta clase te pedimos dos cosas:
* Que recopiles las soluciones de los siguientes ejercicios:

1. El archivo `fileparse.py` del [Ejercicio 6.4](../06_Plt_Especificacion_y_Documentacion/03_Flexibilidad.md#ejercicio-64-de-archivos-a-objetos-cual-archivos).
1. El archivo `informe.py` del [Ejercicio 6.5](../06_Plt_Especificacion_y_Documentacion/03_Flexibilidad.md#ejercicio-65-arreglemos-las-funciones-existentes).
1. El archivo `documentacion.py` del [Ejercicio 6.8](../06_Plt_Especificacion_y_Documentacion/04_Especificacion_y_Documentacion.md#ejercicio-68-funciones-y-documentación).
1. El archivo `random_walk.py` del [Ejercicio 6.10](../06_Plt_Especificacion_y_Documentacion/06_Matplotlib.md#ejercicio-610-caminatas-al-azar).

