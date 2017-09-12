![Logo](http://i.imgur.com/azI7ASc.png)

*TerminKalender Stats* es un proyecto realizado para la **Universidad de Cádiz** con la finalidad de buscar ciertas estadísticas (las cuales se detallan más adelante) referentes al uso del juego/aplicación [TerminKalender](https://github.com/luisrozo/Terminkalender).

## Sobre la aplicación

La aplicación consiste en acordar varias actividades mediante **conversaciones en alemán** y tratar de encuadrarlas en un calendario a modo de agenda.

 Existen dos formas de jugar a TerminKalender:
 - *Versión papel*. Los usuarios se pasan un papel donde se escriben los mensajes. Las conversaciones son transcritas a ficheros Excel.
 - *Versión app*. Los usuarios utilizan el chat de la aplicación para acordar las actividades. Esta app fue desarrollada por [Javier Osuna](https://github.com/javosuher). Las conversaciones quedan guardadas en los *logs* generados por la aplicación.

## Sobre el script

### Instrucciones de uso
Hay dos scripts: uno (*/app/app_stats.py*) para sacar estadísticas de los *logs* generados por la aplicación, y otro (*/paper/paper_stats.py*) para hacer lo mismo pero con las transcripciones de la versión en papel.

Para usar los scripts, seguir los siguientes pasos:

1. Clonar este repositorio usando el siguiente comando en una terminal:
        ```
        git clone https://github.com/luisrozo/tk-stats.git
        ```
        
2. Colocar los ficheros *logs* en la carpeta */app/* a los que se quiera aplicar el script.

3. Igualmente, colocar los ficheros *Excel* en la carpeta */paper/*.

4. Para ejecutar el script *app_stats.py*, abrir una terminal en la carpeta */app/* y ejecutar el siguiente comando:
        ```
        python app_stats.py
        ```
        
5. Para ejecutar el script *paper_stats.py*, abrir una terminal en la carpeta */paper/* y ejecutar el siguiente comando:
        ```
        python paper_stats.py
        ```


### Estadísticas

Las estadísticas buscadas en los chats se dividen en tres grandes categorías:

- Estadísticas globales
- Estadísticas por alumno
- Estadísticas por parejas

A continuación, se listan las estadísticas que se buscan para todas las categorías:

- ~~Tiempo empleado~~
- Palabras
- Palabras distintas
- Palabras correctas/en diccionario
- Palabras correctas distintas
- Palabras incorrectas/fuera de diccionario
- Palabras incorrectas distintas
- Palabras reservadas
- Palabras reservadas distintas
- Palabras reservadas por categoría
- Palabras reservadas distintas por categoría
- Estructuras gramaticales precisas por tipos
- Estructuras gramaticales precisas distintas por tipos
- Estructuras gramaticales similares por tipos
- Estructuras gramaticales similares distintas por tipos
- Frases
- Frases de una sola palabra
- Frases interrogativas
- Frases exclamativas
- Mensajes
- Turnos (unidades)
- ~~Turnos (tiempo)~~
- ~~Actividades en pareja:~~
    - ~~Actividades propuestas~~
    - ~~Actividades acordadas~~
    - ~~Actividades mal acordadas~~
- ~~Actividades en trío:~~
    - ~~Actividades propuestas~~
    - ~~Actividades acordadas~~
    - ~~Actividades mal acordadas~~

Además, para las estadísticas globales y por alumno, se buscarán:
- ~~Actividades individuales:~~
    - ~~Actividades acordadas~~

Para ver qué es exactamente una *palabra reservada* o una *estructura gramatical*, haz click en los respectivos enlaces.

### Preprocesado
Con el fin de determinar estadísticas más cercanas a la realidad y con mayor facilidad, antes de la extracción de estadísticas se realiza un preprocesado, tanto a los logs de la aplicación como a las transcripciones de la versión en papel. Este preprocesado realiza los siguientes cambios:

- Cualquier risa *(por ejemplo: jaja, jeje, jiji, haha...)* y variantes, se normaliza a "*jajaja*".
- Si alguien emplea la palabra *hallo* para saludar, pero añadiendo más 'oes' al final, se normaliza a una sola 'o': *hallo*.
- Del mismo modo, si alguien afirma usando el adverbio de afirmación *Ja*, pero añadiendo más 'aes' al final, se normaliza a una sola 'a': *Ja*.
- El uso de símbolos de interrogación y exclamación intercalados *(por ejemplo: "?!?")*, se normaliza a "*?*".
- La aparición de dos o más almohadillas seguidas *(por ejemplo: "###")*, se normaliza a "*#*".
- Cualquier ristra de signos de interrogación *(por ejemplo: "???")*, se normaliza a " *?*".
- Al igual que el anterior caso, sucede lo mismo con los signos de exclamación. 
- De la misma forma, se hace lo mismo con los asteriscos, aunque añadiendo también un espacio después del mismo: " *\** ".
- Cualquier ristra de puntos que contenga dos o más puntos, se normaliza como puntos suspensivos " *...* ".
- De la misma manera, se hace lo mismo con las comas: " *,* ".
- Todas las vocales que aparezcan tres o más veces seguidas en una palabra, se normaliza a una sola.
- Se quitan todas las comillas.
- Se añaden espacios a la izquierda y a la derecha de todos los paréntesis. "*(Github)*" pasaría a " *(* *Github* *)* ".
- A cada punto (*.*) se le añade un espacio a la izquierda. Las excepciones para este caso son:
    - Dicho punto no pertenece a unos puntos suspensivos (*...*).
    - Dicho punto no pertenece al uso del emoticono de sorpresa (*o.o*).

### Salida del script
El script generará un fichero de texto plano en la carpeta donde se ejecute el mismo que contendrá información sobre las estadísticas que se han encontrado.

