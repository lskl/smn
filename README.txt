Repositorio con scripts para manipular y visualizar datos de estaciones meteorológicas del SMN mexicano.

--------------------------------------------------------------

Los datos primarios se encuentran en formato TXT. Cada archivo incluye un encabezado de varias líneas, con datos generales de la estación. Después los archivos incluyen líneas con datos diarios de 4 variables: 

* Precipitación en milímetros
* Evaporación en milímetros
* Temperatura máxima en grados centígrados
* Temperatura mínima en grados centígrados

No todos los días tienen datos, y no todas las líneas tienen mediciones de las cuatro variables.

Los datos originales se pueden descargar desde la página del Sistema Meteorológico Nacional: https://smn.conagua.gob.mx/es/climatologia/informacion-climatologica/informacion-estadistica-climatologica

Ejemplo de archivo con datos diarios:
https://smn.conagua.gob.mx/tools/RESOURCES/Diarios/8030.txt

--------------------------------------------------------------

En este repositorio se considera que los datos están en el directorio: "../datos". Los datos primarios en formato TXT deben ester en "/datos/datos primarios/Total de estaciones".



