# OBJETIVO DEL PROYECTO

El objetivo de este ejercicio es desarrollar 
un paquete de Python que nos permita resolver
el problema dado.\
\
La implementación debe ser capaz de realizar un
análisis de datos con información genética sobre
el Bacilo de Koch.En particular, nos centramos
en las pautas abiertas de lectura de los genes del 
Bacilo de Koch.

## Estructura del proyecto
La estructura de directorios es la siguiente:

* Scripts: incluye todos los archivos .py con las funciones
  a utilizar durante el análisis
  * El archivo basic.py inlcuye la llamada a todas las 
    funciones en el orden solicitado en el enunciado.
  * En cuanto a las visualizaciones, se crea dentro del archivo scripts
    la carpeta figures en las que se guardan los gráficos.
    
* Data: carpeta destinada a los archivos "inputs" de nuestro programa. Será necesario su creación por parte de los usuarios. Además, se deberán incluir en esta carpeta los ficheros originales proporcionados junto a la práctica:  
  * orfs/tb_data_0x.pl: contiene información detallada sobre todos los genes indicados.
  * tb_functions.pl: contiene información general sobre los genes y sus clases funcionales.
* tests: Incluye varios suites de tests que permiten comprobar el buen funcionamiento de las funciones implementadas.
  * Se ha creado un entorno aislado.Para dar el contexto individual se crea el archivo context.py
* LICENCE.txt: fichero con los datos de la licencia incluida en el proyecto.
* requirements.txt: fichero con la relación de módulos adicionales necesarios para la ejecución del código