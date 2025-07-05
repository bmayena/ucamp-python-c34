# ucamp-python-c34
Bootcamp Python 2025 Brenda Mayén Almaguer
Se realizo la calculadora de índice de masa corporal con los conocimientos obtenidos en el primer módulo de este bootcamp. Los conocimientos que se brindaron durante esta primera etapa y que fueron necesarios para poder realizar un programa básico como el que se presenta son los siguientes:
-Definición y función de las variables dentro de Python.
-Función de input para la obtención de datos
-Uso de la función print y como emplearla de acuerdo a la información que se quiere proyectar. 

Elabore este programa primero definiendo todos los datos que el usuario debe de proporcionar, ya que estas serian nuestras variables para realizar el despliegue de información y el calculo del IMC. 
Durante las pruebas de la función input encontré que era necesario restringir la información que se iba a colocar, por ejemplo en los datos de peso y estatura solo se debían colocar números que podían ser con decimales, por lo que se anido el input a "float" con el fin de evitar colocar caracteres alfabéticos. 
Este mismo problema puede aplicarse al input del nombre, sin embargo no logre restringirlo bajo la misma lógica que con los números, supongo que no basta con colocar un "string" previo al input. 

Definí el imc como una variable también y dentro de su función se empleo la jerarquía de operaciones con las variables de peso y estatura para lograr el cálculo correcto. 

En la elaboración del programa y por una idea errónea que tenia previamente, creí que era necesario un print para pedir el input, pero me di cuenta que no es necesario ya que la acción la realiza el mismo input, por lo que pase estas líneas a comentarios. 

Posteriormente y una vez definidas las variables y agregados los input necesarios, solo se debia mostrar la información con print. Esta parte aunque pareciera sencilla requiere algo de estrategia en el como queremos que muestre la información, por ejemplo en un principio todo estaba sin un formato cómodo de leer y tuve que emplear \n para introducir saltos de línea, posteriormente me explicaron que con el uso de triples comillas podía colocar texto de una forma más cómoda a la escritura convencional. Adicionalmente tuve que tomar en cuenta que habría que hacer una conversión de las variables númericas en el print, por lo que las anide en un str(). Como un extra emple la función round para evitar que el cálculo del IMC quedara con muchos decimales. 

Este ejercicio no solo me ayudo a poner en practica las funciones básicas, me generó muchas más dudas sobre como podría ser más eficiente la programación, me impulso a investigar por ejemplo como podía intentar limitar a que solo aceptara letras en el input de nombre e intentar arrojar un mensaje cuando hubiera algún error y si bien no logré aplicarlo aún al programa, me demuestra que existen muchas maneras de lograr un objetivo y que hay siempre oportunidad de mejora. 
Adicionalmente entendí la importancia de comprender muy bien primero que es lo que quiero lograr y cual es la lógica o mecánica de lo que quiero programar incluso antes de comenzar con la programación, creo que esta parte puede evitar caer en muchos errores durante el proceso.

