#!/usr/bin/env python
# encoding: utf-8

""" Script para buscar estadísticas en los logs de la aplicación TerminKalender.
    Visita la documentación en GitHub para obtener información más detallada.

    Autor: Luis Gonzaga Rozo Bueno. 2017.
"""

import sys
import enchant
import os
import re
import itertools

# Cargar todos los ficheros 'logs' existentes en la carpeta del script
logs = []

for log in os.listdir("."):
    if '(' in log and ')' in log and '.txt' in log and '~' not in log:
        fichero = open(r'./'+log, 'r').readlines()
        logs.append(fichero)

# Preprocesado
for log in logs:
    for line in log:
        linea = line
        laughing = re.findall(r"jaj.*|jej.*|jij.*|joj.*|juj.*|hah.*", linea, re.IGNORECASE)
        if laughing:
            index = log.index(line)
            for replacement in laughing:
                log[index] = linea.replace(replacement, "jajaja")
            linea = log[index]

        greetings = re.findall('hallo*', linea, re.IGNORECASE)
        if greetings:
            index = log.index(linea)
            for replacement in greetings:
                log[index] = linea.replace(replacement, "hallo")
            linea = log[index]

        ja = re.findall('jaa+', linea, re.IGNORECASE)
        if ja:
            index = log.index(linea)
            for replacement in ja:
                log[index] = linea.replace(replacement, "ja")
            linea = log[index]

        anxious = re.findall(r'\?+!+', linea, re.IGNORECASE)
        if anxious:
            index = log.index(linea)
            for replacement in anxious:
                log[index] = linea.replace(replacement, "?")
            linea = log[index]

        sharp = re.findall(r'#+', linea, re.IGNORECASE)
        if sharp:
            index = log.index(linea)
            for replacement in sharp:
                log[index] = linea.replace(replacement, "#")
            linea = log[index]

        interrogation = re.findall(r'\?+', linea, re.IGNORECASE)
        if interrogation:
            index = log.index(linea)
            for replacement in interrogation:
                log[index] = linea.replace(replacement, " ?")
            linea = log[index]

        asterisk = re.findall('\*+', linea, re.IGNORECASE)
        if asterisk:
            index = log.index(linea)
            for replacement in asterisk:
                log[index] = linea.replace(replacement, " * ")
            linea = log[index]

        exclamation = re.findall('\!+', linea, re.IGNORECASE)
        if exclamation:
            index = log.index(linea)
            for replacement in exclamation:
                log[index] = linea.replace(replacement, " !")
            linea = log[index]

        ellipsis = re.findall('\.\.+', linea, re.IGNORECASE)
        if ellipsis:
            index = log.index(linea)
            for replacement in ellipsis:
                log[index] = linea.replace(replacement, " ... ")
            linea = log[index]

        comma = re.findall(',\s?', linea, re.IGNORECASE)
        if comma:
            index = log.index(linea)
            for replacement in comma:
                log[index] = linea.replace(replacement, " , ")
            linea = log[index]

        a_vowel = re.findall('aa+', linea, re.IGNORECASE)
        if a_vowel:
            index = log.index(linea)
            for replacement in a_vowel:
                log[index] = linea.replace(replacement, "a")
            linea = log[index]

        e_vowel = re.findall('ee+', linea, re.IGNORECASE)
        if e_vowel:
            index = log.index(linea)
            for replacement in e_vowel:
                log[index] = linea.replace(replacement, "e")
            linea = log[index]

        i_vowel = re.findall('ii+', linea, re.IGNORECASE)
        if i_vowel:
            index = log.index(linea)
            for replacement in i_vowel:
                log[index] = linea.replace(replacement, "i")
            linea = log[index]

        o_vowel = re.findall('oo+', linea, re.IGNORECASE)
        cool = re.findall('cool', linea, re.IGNORECASE)
        if o_vowel and not cool:
            index = log.index(linea)
            for replacement in o_vowel:
                log[index] = linea.replace(replacement, "o")
            linea = log[index]

        u_vowel = re.findall('uu+', linea, re.IGNORECASE)
        if u_vowel:
            index = log.index(linea)
            for replacement in u_vowel:
                log[index] = linea.replace(replacement, "u")
            linea = log[index]

        marks = re.findall('"', linea, re.IGNORECASE)
        if marks:
            index = log.index(linea)
            for replacement in marks:
                log[index] = linea.replace(replacement, "")
            linea = log[index]

        l_paren = re.findall('\(', linea, re.IGNORECASE)
        if l_paren:
            index = log.index(linea)
            for replacement in l_paren:
                log[index] = linea.replace(replacement, " ( ")
            linea = log[index]

        r_paren = re.findall('\)', linea, re.IGNORECASE)
        if r_paren:
            index = log.index(linea)
            for replacement in r_paren:
                log[index] = linea.replace(replacement, " ) ")
            linea = log[index]

        point = re.findall('\.', linea, re.IGNORECASE)
        shocked = re.findall('o.o', linea, re.IGNORECASE)
        if point and not ellipsis and not shocked:
            index = log.index(linea)
            for replacement in point:
                log[index] = linea.replace(replacement, " .")
            linea = log[index]

# Para obtener las estadisticas referentes a palabras o expresiones reservadas, se hace uso de la siguientes estructuras

pronombres_interrogativos = ["mit wem", "um wie viel Uhr", "um wieviel Uhr", "wann", "was", "wer", "wie",
                             "wo", "wohin"]

adjetivos = ["frei", "gestresst", "hungrig", "müde", "happy", "glücklich"]

saludos_despedidas = ["auf Wiedersehen!", "bis Montag", "bis Dienstag",
                      "bis Mittwoch", "bis Donnerstag", "bis Freitag", "bis Samstag", "bis Sonntag",
                      "bis bald", "bis dann", "bis später",
                      "ciao", "hallihallo", "hallo", "hey", "hi", "mach's gut", "tschüs",
                      "tschüs, bis bald", "tschüs, bis dann", "tschüs, bis später", "tschüss",
                      "tschüss, bis bald",
                      "tschüss, bis dann", "tschüss, bis später",
                      "tschüs bis bald", "tschüs bis dann", "tschüs bis später", "tschüss bis bald",
                      "tschüss bis dann", "tschüss bis später"]

frases_hechas = ["ich bin gestresst", "ich bin happy", "ich bin relaxt", "ich bin hungirg",
                 "ich bin frustriert",
                 "ich bin deprimiert", "ich bin alleine", "ich bin müde", "ich bin fit",
                 "ich bin total fit",
                 "ich habe Zeit",
                 "ich habe keine Zeit",
                 "ich habe leider keine Zeit",
                 "mir geht's gut", "mir geht's schlecht", "mir geht's so lala", "mir geht's fatal",
                 "mir geht's super",
                 "mir geht's total super", "mir geht's phantastisch", "mir geht's fantastisch",
                 "mir geht's wunderbar",
                 "mir geht's genial", "mir geht's total gut", "mir geht's total schlecht",
                 "mir geht's spitze"]

expresiones_afirmacion = ["alles klar", "das ist gut", "genial", "gut", "ja, cool", "ja cool", "ja, klar",
                          "ja klar",
                          "ja, klasse", "ja klasse", "ja, natürlich", "ja natürlich", "ja, perfekt",
                          "ja perfekt",
                          "ja, phantastisch", "ja phantastisch", "ja, super Idee", "ja super Idee",
                          "ja, super", "ja super", "ja, wunderbar", "ja wunderbar", "kein Problem", "klasse",
                          "ok",
                          "okay", "super", "total super"]

expresiones_negacion_duda = ["nein", "ne", "nee", "neee", "keine Ahnung", "ich weiss nicht",
                             "ich habe keine Ahnung", "hm"]

lugares = ["Bibliothek", "Café", "Copyshop", "Copycenter", "Disco", "Disko", "Diskothek", "Einkaufszentrum",
           "Eiscafé", "Fitnessstudio", "Fitnesszentrum", "Fussballplatz", "Fußballplatz", "Fussballstadion",
           "Fußballstadion", "Fussballstadium", "Fußballstadium", "Kino", "Kneipe", "Konzert", "Pub",
           "Restaurant",
           "Schwimmbad", "Sportzentrum", "Strand", "Supermarkt", "Tennisplatz", "Theater", "Uni",
           "Universität",
           "Zentrum", "zu Hause", "zuhause"]

dias_de_la_semana = ["Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag", "Wochenende"]

adverbios_temporales = ["am Montagmorgen", "am Montagvormittag", "am Montagmittag",
                        "am Montagnachmittag", "am Montagabend", "am Dienstagmorgen", "am Dienstagvormittag",
                        "am Dienstagmittag", "am Dienstagnachmittag", "am Dienstagabend", "am Mittwochmorgen",
                        "am Mittwochvormittag", "am Mittwochmittag", "am Mittwochnachmittag",
                        "am Mittwochabend",
                        "am Donnerstagmorgen", "am Donnerstagvormittag", "am Donnerstagmittag",
                        "am Donnerstagnachmittag", "am Donnerstagabend", "am Freitagmorgen",
                        "am Freitagvormittag",
                        "am Freitagmittag", "am Freitagnachmittag", "am Freitagabend", "am Samstagmorgen",
                        "am Samstagvormittag", "am Samstagmittag", "am Samstagnachmittag", "am Samstagabend",
                        "am Sonntagmorgen", "am Sonntagvormittag", "am Sonntagmittag", "am Sonntagnachmittag",
                        "am Sonntagabend",
                        "Montagnacht", "Dienstagnacht", "Mittwochnacht", "Donnerstagnacht",
                        "Freitagnacht", "Samstagnacht", "Sonntagnacht",
                        'montagmorgens', 'montagvormittags', 'montagmittags', 'montagnachmittags',
                        'montagabends',
                        'montagnachts', 'dienstagmorgens', 'dienstagvormittags', 'dienstagmittags',
                        'dienstagnachmittags', 'dienstagabends', 'dienstagnachts', 'mittwochmorgens',
                        'mittwochvormittags', 'mittwochmittags', 'mittwochnachmittags', 'mittwochabends',
                        'mittwochnachts', 'donnerstagmorgens', 'donnerstagvormittags', 'donnerstagmittags',
                        'donnerstagnachmittags', 'donnerstagabends', 'donnerstagnachts', 'freitagmorgens',
                        'freitagvormittags', 'freitagmittags', 'freitagnachmittags', 'freitagabends',
                        'freitagnachts',
                        'samstagmorgens', 'samstagvormittags', 'samstagmittags', 'samstagnachmittags',
                        'samstagabends',
                        'samstagnachts', 'sonntagmorgens', 'sonntagvormittags', 'sonntagmittags',
                        'sonntagnachmittags',
                        'sonntagabends', 'sonntagnachts',
                        "am Vormittag", "am Mittag", "am Nachmittag", "am Abend", "in der Nacht", "am Montag",
                        "am Dienstag", "am Mittwoch", "am Donnerstag", "am Freitag", "am Samstag", "am Sonntag"]

horas = ["um 1 Uhr", "um 2 Uhr", "um 3 Uhr", "um 4 Uhr", "um 5 Uhr", "um 6 Uhr", "um 7 Uhr", "um 8 Uhr",
         "um 9 Uhr", "um 10 Uhr", "um 11 Uhr", "um 12 Uhr", "um 13 Uhr", "um 14 Uhr", "um 15 Uhr", "um 16 Uhr",
         "um 17 Uhr", "um 18 Uhr", "um 19 Uhr", "um 20 Uhr", "um 21 Uhr", "um 22 Uhr", "um 23 Uhr", "um 24 Uhr",
         'um 1', 'um 2', 'um 3', 'um 4', 'um 5', 'um 6', 'um 7', 'um 8', 'um 9', 'um 10', 'um 11', 'um 12',
         'um 13', 'um 14', 'um 15', 'um 16', 'um 17', 'um 18', 'um 19', 'um 20', 'um 21', 'um 22', 'um 23', 'um 24',
         "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
         "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig",
         "einundzwanzig",
         "zweiundzwanzig", "dreiundzwanzig", "vierundzwanzig",
         'um ein', 'um zwei', 'um drei', 'um vier', 'um fünf', 'um sechs', 'um sieben', 'um acht', 'um neun',
         'um zehn', 'um elf', 'um zwölf', 'um dreizehn', 'um vierzehn', 'um fünfzehn', 'um sechzehn',
         'um siebzehn', 'um achtzehn', 'um neunzehn', 'um zwanzig', 'um einundzwanzig', 'um zweiundzwanzig',
         'um dreiundzwanzig', 'um vierundzwanzig']

preposicion_mit = ["mit"]

preposiciones_con_pronombres_personales = ["mit mir", "mit dir", "mit uns"]

''' Nuevas estructuras '''

''' '''

# Si se añaden nuevos tipos de palabras o expresiones reservadas, añadirlo tambien en estas dos estructuras.

tipos_expresiones = ["Pronombre interrogativo", "Adjetivo", "Saludo o despedida", "Frase hecha",
                     "Expresion de afirmacion", "Expresion de negacion o duda", "Lugar", "Dia de la semana",
                     "Adverbio temporal", "Hora", "Preposicion mit", "Preposicion con pronombre personal"]

array_expresiones = [pronombres_interrogativos, adjetivos, saludos_despedidas, frases_hechas,
                     expresiones_afirmacion, expresiones_negacion_duda, lugares, dias_de_la_semana,
                     adverbios_temporales, horas, preposicion_mit, preposiciones_con_pronombres_personales]

# Para tener en cuenta las mayusculas o minusculas en las busquedas, se hara uso de esta lista de sustantivos:

sustantivos = ["Abend", "Ahnung", "Bibliothek", "Café", "Copycenter", "Copyshop", "Dienstag", "Dienstagnacht",
               "Disco",
               "Disko", "Diskothek", "Donnerstag", "Donnerstagnacht", "Einkaufszentrum", "Eiscafé",
               "Fitnessstudio",
               "Fitnesszentrum", "Freitag", "Freitagnacht", "Fussballplatz", "Fußballplatz", "Fussballstadion",
               "Fußballstadion", "Fussballstadium", "Fußballstadium", "Idee", "Kino", "Kneipe", "Konzert",
               "Mittag",
               "Mittwoch", "Mittwochnacht", "Montag", "Montagnacht", "Nachmittag", "Nacht", "Problem", "Pub",
               "Restaurant", "Samstag", "Samstagnacht", "Schwimmbad", "Sonntag", "Sonntagnacht", "Sportzentrum",
               "Strand", "Supermarkt", "Tennisplatz", "Theater", "Uhr", "Uni", "Universität", "Vormittag",
               "Wochenende",
               "Zeit", "Zentrum", "zu Hause", "zuhause"]


# Para buscar estas expresiones en los logs, se llama a la funcion usaExpresionReservada().

def usaExpresionReservada(frase):
    # El array expresionesUtilizadas contendra tuplas de la forma [Tipo de expresion, expresion]
    expresionesUtilizadas = []
    # La variable 'i' ayuda a obtener el tipo de la expresion que se ha detectado
    i = 0
    for tipo_expresion in array_expresiones:
        for expresion in tipo_expresion:
            sustantivos_utilizados = []
            sustantivos_minusculas = []
            busqueda_refinada = False

            # Determinamos si hacer busqueda refinada, y guardamos los sustantivos (bien o mal) utilizados en la frase.
            for sustantivo in sustantivos:
                sustantivo_encontrado = re.findall(r'\b' + sustantivo + r'\b', frase, re.IGNORECASE)
                for sust in sustantivo_encontrado:
                    if sust.istitle():  # Sustantivo bien utilizado
                        sustantivos_utilizados.append(sust)
                        busqueda_refinada = True
                    else:
                        sustantivos_minusculas.append(sust)

            # Se pasa la frase a minusuculas, dejando solamente los sustantivos en mayuscula.
            if busqueda_refinada:
                frase = frase.lower()
                for sustantivo in sustantivos_utilizados:
                    sustitucion = re.findall(r'\b' + sustantivo + r'\b', frase, re.IGNORECASE)
                    frase = frase.replace(sustitucion[0], sustantivo)

                if expresion in frase:
                    expresionesUtilizadas.append([tipos_expresiones[i], expresion])

            # Se compara con la frase original o con la frase en minusculas, eliminando los sustantivos mal utilizados.
            else:
                frase_split = frase.split()
                for sust in sustantivos_minusculas:
                    frase_split.remove(sust)
                frase_completa = ' '.join(frase_split)

                expr = re.findall(r'\b'+expresion+r'\b', frase_completa, re.IGNORECASE)
                if expr:
                    expresionesUtilizadas.append([tipos_expresiones[i], expresion])
        i += 1

    return expresionesUtilizadas

# Esta ampliación de diccionario contiene palabras que el módulo 'enchant' no
# considera correctas para el diccionario alemán, pero no son incorrectas al tratarse
# de nombres de lugares, actividades, etc., que se utilizan en los chats para concretar
# los planes.
ampliacion_diccionario = []
lista_manual = ["Ah", "ah", "Ahh", "ahh", "Disco", "jajaja", "Mmm", "mmm", "ok"]

try:
    fichero_con_tareas = open(r'../tasks.xml', 'r').readlines()
    for linea in fichero_con_tareas:
        if '<field>' in linea:
            palabras = re.sub(r'<field>|\(|\)|</field>', '', linea).split()
            for palabra in palabras:
                ampliacion_diccionario.append(palabra.title())
                ampliacion_diccionario.append(palabra.lower())
except IOError:
    print "Falta el fichero tasks.xml; consulta la sección \"Sobre el script - Instrucciones de uso\" " \
          "para más información."
    sys.exit()

for palabra in lista_manual:
    ampliacion_diccionario.append(palabra)

for adv in adverbios_temporales:
    ampliacion_diccionario.append(adv)

ampliacion_diccionario = sorted(set(ampliacion_diccionario))


class Actividad:
    def __init__(self, nombre_act, autor, partners, position, what_exactly, where, where_exactly, trio):
        self.nombre_act = nombre_act
        self.autor = autor
        self.partners = partners
        self.position = position
        self.what_exactly = what_exactly
        self.where = where
        self.where_exactly = where_exactly
        self.trio = trio

    def __str__(self):
        print "--------------------------"
        print "Nombre de actividad: " + self.nombre_act
        print "Autor: " + self.autor
        print "Partners: " + self.partners
        print "Position: " + self.position
        print "What exactly: " + self.what_exactly
        print "Where: " + self.where
        print "Where exactly: " + self.where_exactly
        print "Trio: " + str(self.trio)
        print "--------------------------"


""" ↓ EXTRACCIÓN DE ESTADÍSTICAS ↓ """

# Extracción de nombres alumnos para estadísticas por alumnos y por pareja.
alumnos = []
parejas = []
for log in logs:
    for line in log:
        if "------------ " in line and len(line.split()) > 5:
            primer_nombre = line.split()[1] + " " + line.split()[2]
            if primer_nombre not in alumnos:
                alumnos.append(primer_nombre)

            segundo_nombre = line.split()[4] + " " + line.split()[5]
            if segundo_nombre not in alumnos:
                alumnos.append(segundo_nombre)

            pareja = primer_nombre + "-" + segundo_nombre
            if pareja not in parejas:
                parejas.append(pareja)

lineas_actividades_grupo = []
lineas_actividades_individuales = []
for log in logs:
    index_tasks = log.index("TASKS \n")
    if "------------ Individuelle Aktivit\xc3\xa4ten ------------ \n" in log:
        index_individuales = log.index("------------ Individuelle Aktivit\xc3\xa4ten ------------ \n")
        lineas_actividades_grupo.append(log[index_tasks:index_individuales])
        lineas_actividades_individuales.append(log[index_individuales:])
    else:
        lineas_actividades_grupo.append(log[index_tasks:])

trios = []
linea_anterior = ""
for lines in lineas_actividades_grupo:
    for line in lines:
        if "----->" in linea_anterior:
            if len(line.split()) > 4:
                alumno1 = linea_anterior.split()[1] + " " + linea_anterior.split()[2]
                alumno2 = line.split()[1] + " " + line.split()[2]
                alumno3 = line.split()[4] + " " + line.split()[5]
                trio = (alumno1 + "-" + alumno2 + "-" + alumno3)
                trios.append(trio)

        linea_anterior = line

stats_per_student = {}
stats_per_pair = {}

# Se utiliza un array para almacenar las estadisticas por estudiante y por pareja.
# Para ello, se le asigna dicho vector a cada entrada del diccionario, respondiendo a los siguientes indices:
# 0: Mensajes
# 1: Frases
# 2: Turnos (en unidades)
# 3: Palabras
# 4: Palabras en diccionario
# 5: Palabras fuera diccionario
# 6: Palabras distintas
# 7: Palabras en diccionario distintas
# 8: Palabras fuera diccionario distintas
# 9: Palabras reservadas total
# 10: Palabras reservadas - Categoría "Pronombres interrogativos"
# 11: Palabras reservadas - Categoría "Adjetivos"
# 12: Palabras reservadas - Categoría "Saludos y despedidas"
# 13: Palabras reservadas - Categoría "Frases hechas"
# 14: Palabras reservadas - Categoría "Expresiones de afirmación"
# 15: Palabras reservadas - Categoría "Expresiones de negación/duda"
# 16: Palabras reservadas - Categoría "Lugares"
# 17: Palabras reservadas - Categoría "Días de la semana"
# 18: Palabras reservadas - Categoría "Adverbios temporales"
# 19: Palabras reservadas - Categoría "Horas"
# 20: Palabras reservadas - Categoría "Preposición 'mit'"
# 21: Palabras reservadas - Categoría "'Mit' + pronombres personales"
# 22: Palabras reservadas distintas
# 23: Palabras reservadas distintas - Categoría "Pronombres interrogativos"
# 24: Palabras reservadas distintas - Categoría "Adjetivos"
# 25: Palabras reservadas distintas - Categoría "Saludos y despedidas"
# 26: Palabras reservadas distintas - Categoría "Frases hechas"
# 27: Palabras reservadas distintas - Categoría "Expresiones de afirmación"
# 28: Palabras reservadas distintas - Categoría "Expresiones de negación/duda"
# 29: Palabras reservadas distintas - Categoría "Lugares"
# 30: Palabras reservadas distintas - Categoría "Días de la semana"
# 31: Palabras reservadas distintas - Categoría "Adverbios temporales"
# 32: Palabras reservadas distintas - Categoría "Horas"
# 33: Palabras reservadas distintas - Categoría "Preposición 'mit'"
# 34: Palabras reservadas distintas - Categoría "'Mit' + pronombres personales"
# 35: Frases de una sola palabra
# 36: Frases interrogativas
# 37: Frases exclamativas
# 38: Estructuras gramaticales precisas total
# 39: Estructuras gramaticales precisas - Categoría "Preguntas con Complemento de Lugar"
# 40: Estructuras gramaticales precisas - Categoría "Preguntas con Complemento de Tiempo"
# 41: Estructuras gramaticales precisas - Categoría "Preguntas simples"
# 42: Estructuras gramaticales precisas - Categoría "Enunciados con Complemento Directo"
# 43: Estructuras gramaticales precisas distintas
# 44: Estructuras gramaticales precisas distintas - Categoría "Preguntas con Complemento de Lugar"
# 45: Estructuras gramaticales precisas distintas - Categoría "Preguntas con Complemento de Tiempo"
# 46: Estructuras gramaticales precisas distintas - Categoría "Preguntas simples"
# 47: Estructuras gramaticales precisas distintas - Categoría "Enunciados con Complemento Directo"
# 48: Estructuras gramaticales similares total
# 49: Estructuras gramaticales similares - Categoría "Preguntas con Complemento de Lugar"
# 50: Estructuras gramaticales similares - Categoría "Preguntas con Complemento de Tiempo"
# 51: Estructuras gramaticales similares - Categoría "Preguntas simples"
# 52: Estructuras gramaticales similares - Categoría "Enunciados con Complemento Directo"
# 53: Estructuras gramaticales similares distintas
# 54: Estructuras gramaticales similares distintas - Categoría "Preguntas con Complemento de Lugar"
# 55: Estructuras gramaticales similares distintas - Categoría "Preguntas con Complemento de Tiempo"
# 56: Estructuras gramaticales similares distintas - Categoría "Preguntas simples"
# 57: Estructuras gramaticales similares distintas - Categoría "Enunciados con Complemento Directo"
# 58: Actividades propuestas en pareja
# 59: Actividades acordadas en pareja
# 60: Actividades mal acordadas en pareja
''' Las siguientes estadísticas sólo están disponibles para estadísticas por alumno '''
# 61: Actividades propuestas en trío
# 62: Actividades acordadas en trío
# 63: Actividades mal acordadas en trío
# 64: Actividades acordadas individualmente


for alumno in alumnos:
    stats_per_student[alumno] = [["Mensajes", ], ["Frases", ], ["Turnos (unidades)", 0],
                                 ["Palabras", ], ["Palabras en diccionario", ], ["Palabras fuera diccionario", ],
                                 ["Palabras distintas", ], ["Palabras en diccionario distintas", ], ["Palabras fuera diccionario distintas", ],
                                 ["Palabras reservadas total", ],
                                 ["Palabras reservadas - Categoría \"Pronombres interrogativos\"", ],
                                 ["Palabras reservadas - Categoría \"Adjetivos\"", ],
                                 ["Palabras reservadas - Categoría \"Saludos y despedidas\"", ],
                                 ["Palabras reservadas - Categoría \"Frases hechas\"", ],
                                 ["Palabras reservadas - Categoría \"Expresiones de afirmación\"", ],
                                 ["Palabras reservadas - Categoría \"Expresiones de negación/duda\"", ],
                                 ["Palabras reservadas - Categoría \"Lugares\"", ],
                                 ["Palabras reservadas - Categoría \"Días de la semana\"", ],
                                 ["Palabras reservadas - Categoría \"Adverbios temporales\"", ],
                                 ["Palabras reservadas - Categoría \"Horas\"", ],
                                 ["Palabras reservadas - Categoría \"Preposición 'mit'\"", ],
                                 ["Palabras reservadas - Categoría \"'Mit' + pronombres personales\"", ],
                                 ["Palabras reservadas distintas", ],
                                 ["Palabras reservadas distintas - Categoría \"Pronombres interrogativos\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Adjetivos\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Saludos y despedidas\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Frases hechas\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Expresiones de afirmación\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Expresiones de negación/duda\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Lugares\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Días de la semana\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Adverbios temporales\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Horas\"", ],
                                 ["Palabras reservadas distintas - Categoría \"Preposición 'mit'\"", ],
                                 ["Palabras reservadas distintas - Categoría \"'Mit' + pronombres personales\"", ],
                                 ["Frases de una sola palabra", ], ["Frases interrogativas", ], ["Frases exclamativas", ],
                                 ["Estructuras gramaticales precisas total", ],
                                 ["Estructuras gramaticales precisas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                                 ["Estructuras gramaticales precisas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                                 ["Estructuras gramaticales precisas - Categoría \"Preguntas simples\"", ],
                                 ["Estructuras gramaticales precisas - Categoría \"Enunciados con Complemento Directo\"", ],
                                 ["Estructuras gramaticales precisas distintas", ],
                                 ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                                 ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                                 ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas simples\"", ],
                                 ["Estructuras gramaticales precisas distintas - Categoría \"Enunciados con Complemento Directo\"", ],
                                 ["Estructuras gramaticales similares total", ],
                                 ["Estructuras gramaticales similares - Categoría \"Preguntas con Complemento de Lugar\"", ],
                                 ["Estructuras gramaticales similares - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                                 ["Estructuras gramaticales similares - Categoría \"Preguntas simples\"", ],
                                 ["Estructuras gramaticales similares - Categoría \"Enunciados con Complemento Directo\"", ],
                                 ["Estructuras gramaticales similares distintas", ],
                                 ["Estructuras gramaticales similares distintas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                                 ["Estructuras gramaticales similares distintas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                                 ["Estructuras gramaticales similares distintas - Categoría \"Preguntas simples\"", ],
                                 ["Estructuras gramaticales similares distintas - Categoría \"Enunciados con Complemento Directo\"", ],
                                 ["Actividades propuestas en pareja", ],
                                 ["Actividades acordadas en pareja", ],
                                 ["Actividades mal acordadas en pareja", ],
                                 ["Actividades propuestas en trio", ],
                                 ["Actividades acordadas en trio", ],
                                 ["Actividades mal acordadas en trio", ],
                                 ["Actividades acordadas individualmente", ],
                                 ]

for pareja in parejas:
    stats_per_pair[pareja] = [["Mensajes", ], ["Frases", ], ["Turnos (unidades)", 0],
                              ["Palabras", ], ["Palabras en diccionario", ], ["Palabras fuera diccionario", ],
                              ["Palabras distintas", ], ["Palabras en diccionario distintas", ], ["Palabras fuera diccionario distintas", ],
                              ["Palabras reservadas total", ],
                              ["Palabras reservadas - Categoría \"Pronombres interrogativos\"", ],
                              ["Palabras reservadas - Categoría \"Adjetivos\"", ],
                              ["Palabras reservadas - Categoría \"Saludos y despedidas\"", ],
                              ["Palabras reservadas - Categoría \"Frases hechas\"", ],
                              ["Palabras reservadas - Categoría \"Expresiones de afirmación\"", ],
                              ["Palabras reservadas - Categoría \"Expresiones de negación/duda\"", ],
                              ["Palabras reservadas - Categoría \"Lugares\"", ],
                              ["Palabras reservadas - Categoría \"Días de la semana\"", ],
                              ["Palabras reservadas - Categoría \"Adverbios temporales\"", ],
                              ["Palabras reservadas - Categoría \"Horas\"", ],
                              ["Palabras reservadas - Categoría \"Preposición 'mit'\"", ],
                              ["Palabras reservadas - Categoría \"'Mit' + pronombres personales\"", ],
                              ["Palabras reservadas distintas", ],
                              ["Palabras reservadas distintas - Categoría \"Pronombres interrogativos\"", ],
                              ["Palabras reservadas distintas - Categoría \"Adjetivos\"", ],
                              ["Palabras reservadas distintas - Categoría \"Saludos y despedidas\"", ],
                              ["Palabras reservadas distintas - Categoría \"Frases hechas\"", ],
                              ["Palabras reservadas distintas - Categoría \"Expresiones de afirmación\"", ],
                              ["Palabras reservadas distintas - Categoría \"Expresiones de negación/duda\"", ],
                              ["Palabras reservadas distintas - Categoría \"Lugares\"", ],
                              ["Palabras reservadas distintas - Categoría \"Días de la semana\"", ],
                              ["Palabras reservadas distintas - Categoría \"Adverbios temporales\"", ],
                              ["Palabras reservadas distintas - Categoría \"Horas\"", ],
                              ["Palabras reservadas distintas - Categoría \"Preposición 'mit'\"", ],
                              ["Palabras reservadas distintas - Categoría \"'Mit' + pronombres personales\"", ],
                              ["Frases de una sola palabra", ], ["Frases interrogativas", ], ["Frases exclamativas", ],
                              ["Estructuras gramaticales precisas total", ],
                              ["Estructuras gramaticales precisas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                              ["Estructuras gramaticales precisas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                              ["Estructuras gramaticales precisas - Categoría \"Preguntas simples\"", ],
                              ["Estructuras gramaticales precisas - Categoría \"Enunciados con Complemento Directo\"", ],
                              ["Estructuras gramaticales precisas distintas", ],
                              ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                              ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                              ["Estructuras gramaticales precisas distintas - Categoría \"Preguntas simples\"", ],
                              ["Estructuras gramaticales precisas distintas - Categoría \"Enunciados con Complemento Directo\"", ],
                              ["Estructuras gramaticales similares total", ],
                              ["Estructuras gramaticales similares - Categoría \"Preguntas con Complemento de Lugar\"", ],
                              ["Estructuras gramaticales similares - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                              ["Estructuras gramaticales similares - Categoría \"Preguntas simples\"", ],
                              ["Estructuras gramaticales similares - Categoría \"Enunciados con Complemento Directo\"", ],
                              ["Estructuras gramaticales similares distintas", ],
                              ["Estructuras gramaticales similares distintas - Categoría \"Preguntas con Complemento de Lugar\"", ],
                              ["Estructuras gramaticales similares distintas - Categoría \"Preguntas con Complemento de Tiempo\"", ],
                              ["Estructuras gramaticales similares distintas - Categoría \"Preguntas simples\"", ],
                              ["Estructuras gramaticales similares distintas - Categoría \"Enunciados con Complemento Directo\"", ],
                              ["Actividades propuestas en pareja", ],
                              ["Actividades acordadas en pareja", ],
                              ["Actividades mal acordadas en pareja", ],
                              ]

# Adicionalmente, se utilizará un diccionario para las estadísticas en trío con los siguientes índices:
# 0: Actividades propuestas en trio
# 1: Actividades acordadas en trio
# 2: Actividades mal acordadas en trio
actividades_por_trios = {}

for trio in trios:
    actividades_por_trios[trio] = [["Actividades propuestas en trio", ],
                                   ["Actividades acordadas en trio", ],
                                   ["Actividades mal acordadas en trio", ],
                                   ]


# Obtención de mensajes, frases y turnos
mensajes = []
frases = []
frases_una_palabra = []
frases_interrogativas = []
frases_exclamativas = []
pareja_actual = ''
linea_anterior = '-'
numero_turnos = 0
tiempo_turnos = []

# Palabras y corrección según diccionario
palabras = []
palabras_en_diccionario = []
palabras_fuera_diccionario = []
palabras_distintas = []
palabras_en_diccionario_distintas = []
palabras_fuera_diccionario_distintas = []
caracteres_especiales = ["?", "!", ",", ".", "#", "*", "O.o", "(", ")"]
d = enchant.Dict("de_DE")

# Palabras reservadas
palabras_reservadas_total = []
palabras_reservadas_catPronombresInterrogativos = []
palabras_reservadas_catAdjetivos = []
palabras_reservadas_catSaludosDespedidas = []
palabras_reservadas_catFrasesHechas = []
palabras_reservadas_catExpresionesAfirmacion = []
palabras_reservadas_catExpresionesNegacionDuda = []
palabras_reservadas_catLugares = []
palabras_reservadas_catDiasSemana = []
palabras_reservadas_catAdverbiosTemporales = []
palabras_reservadas_catHoras = []
palabras_reservadas_catMit = []
palabras_reservadas_catPronombresPersonales = []
palabras_reservadas_total_por_categoria = [palabras_reservadas_catPronombresInterrogativos,
                                           palabras_reservadas_catAdjetivos,
                                           palabras_reservadas_catSaludosDespedidas,
                                           palabras_reservadas_catFrasesHechas,
                                           palabras_reservadas_catExpresionesAfirmacion,
                                           palabras_reservadas_catExpresionesNegacionDuda,
                                           palabras_reservadas_catLugares,
                                           palabras_reservadas_catDiasSemana,
                                           palabras_reservadas_catAdverbiosTemporales,
                                           palabras_reservadas_catHoras,
                                           palabras_reservadas_catMit,
                                           palabras_reservadas_catPronombresPersonales]

palabras_reservadas_distintas = []
palabras_reservadas_catPronombresInterrogativos_distintas = []
palabras_reservadas_catAdjetivos_distintas = []
palabras_reservadas_catSaludosDespedidas_distintas = []
palabras_reservadas_catFrasesHechas_distintas = []
palabras_reservadas_catExpresionesAfirmacion_distintas = []
palabras_reservadas_catExpresionesNegacionDuda_distintas = []
palabras_reservadas_catLugares_distintas = []
palabras_reservadas_catDiasSemana_distintas = []
palabras_reservadas_catAdverbiosTemporales_distintas = []
palabras_reservadas_catHoras_distintas = []
palabras_reservadas_catMit_distintas = []
palabras_reservadas_catPronombresPersonales_distintas = []
palabras_reservadas_distintas_por_categoria = [palabras_reservadas_catPronombresInterrogativos_distintas,
                                               palabras_reservadas_catAdjetivos_distintas,
                                               palabras_reservadas_catSaludosDespedidas_distintas,
                                               palabras_reservadas_catFrasesHechas_distintas,
                                               palabras_reservadas_catExpresionesAfirmacion_distintas,
                                               palabras_reservadas_catExpresionesNegacionDuda_distintas,
                                               palabras_reservadas_catLugares_distintas,
                                               palabras_reservadas_catDiasSemana_distintas,
                                               palabras_reservadas_catAdverbiosTemporales_distintas,
                                               palabras_reservadas_catHoras_distintas,
                                               palabras_reservadas_catMit_distintas,
                                               palabras_reservadas_catPronombresPersonales_distintas]

# Estructuras gramaticales
estructuras_gramaticales_precisas_total = []
estructuras_gramaticales_precisas_catPreguntasCLugar = []
estructuras_gramaticales_precisas_catPreguntasCTiempo = []
estructuras_gramaticales_precisas_catPreguntasSimples = []
estructuras_gramaticales_precisas_catEnunciadosCDirecto = []
estructuras_gramaticales_precisas_total_por_categoria = [estructuras_gramaticales_precisas_catPreguntasCLugar,
                                                         estructuras_gramaticales_precisas_catPreguntasCTiempo,
                                                         estructuras_gramaticales_precisas_catPreguntasSimples,
                                                         estructuras_gramaticales_precisas_catEnunciadosCDirecto]

estructuras_gramaticales_precisas_distintas = []
estructuras_gramaticales_precisas_catPreguntasCLugar_distintas = []
estructuras_gramaticales_precisas_catPreguntasCTiempo_distintas = []
estructuras_gramaticales_precisas_catPreguntasSimples_distintas = []
estructuras_gramaticales_precisas_catEnunciadosCDirecto_distintas = []
estructuras_gramaticales_precisas_distintas_por_categoria = [estructuras_gramaticales_precisas_catPreguntasCLugar_distintas,
                                                             estructuras_gramaticales_precisas_catPreguntasCTiempo_distintas,
                                                             estructuras_gramaticales_precisas_catPreguntasSimples_distintas,
                                                             estructuras_gramaticales_precisas_catEnunciadosCDirecto_distintas]

estructuras_gramaticales_similares_total = []
estructuras_gramaticales_similares_catPreguntasCLugar = []
estructuras_gramaticales_similares_catPreguntasCTiempo = []
estructuras_gramaticales_similares_catPreguntasSimples = []
estructuras_gramaticales_similares_catEnunciadosCDirecto = []
estructuras_gramaticales_similares_total_por_categoria = [estructuras_gramaticales_similares_catPreguntasCLugar,
                                                         estructuras_gramaticales_similares_catPreguntasCTiempo,
                                                         estructuras_gramaticales_similares_catPreguntasSimples,
                                                         estructuras_gramaticales_similares_catEnunciadosCDirecto]

estructuras_gramaticales_similares_distintas = []
estructuras_gramaticales_similares_catPreguntasCLugar_distintas = []
estructuras_gramaticales_similares_catPreguntasCTiempo_distintas = []
estructuras_gramaticales_similares_catPreguntasSimples_distintas = []
estructuras_gramaticales_similares_catEnunciadosCDirecto_distintas = []
estructuras_gramaticales_similares_distintas_por_categoria = [estructuras_gramaticales_similares_catPreguntasCLugar_distintas,
                                                             estructuras_gramaticales_similares_catPreguntasCTiempo_distintas,
                                                             estructuras_gramaticales_similares_catPreguntasSimples_distintas,
                                                             estructuras_gramaticales_similares_catEnunciadosCDirecto_distintas]

# Actividades en pareja
actividades_propuestas_pareja = []
actividades_acordadas_pareja = []
actividades_mal_acordadas_pareja = []

# Actividades en trío
actividades_propuestas_trio = []
actividades_acordadas_trio = []
actividades_mal_acordadas_trio = []

# Actividades individuales (solo estadísticas general y por alumno)
actividades_acordadas_individuales = []

for log in logs:
    for line in log:
        if "------------ " in line and len(line.split()) > 5:
            pareja_actual = line.split()[1] + " " + line.split()[2] + "-" + line.split()[4] + " " + line.split()[5]
        elif line.startswith(":", 2, 3):
            linea_dividida = line.split()
            linea_anterior_dividida = linea_anterior.split()
            nombre = (linea_dividida[2] + " " + linea_dividida[3]).rstrip(":")

            # Mensajes
            mensaje = ' '.join(linea_dividida[4:])

            mensajes.append(mensaje)
            stats_per_student[nombre][0].append(mensaje)
            stats_per_pair[pareja_actual][0].append(mensaje)

            # Frases
            frases_del_mensaje = []
            if "!" in mensaje:
                if mensaje.index("!") != len(mensaje) - 1:
                    frase = mensaje.split("! ")
                    for f in frase:
                        if frase.index(f) != len(frase) - 1:
                            frases.append(f + "!")
                            stats_per_student[nombre][1].append(f + "!")
                            stats_per_pair[pareja_actual][1].append(f + "!")
                            frases_del_mensaje.append(f + "!")
                        else:
                            frases.append(f)
                            stats_per_student[nombre][1].append(f)
                            stats_per_pair[pareja_actual][1].append(f)
                            frases_del_mensaje.append(f)
                else:
                    frases.append(mensaje)
                    stats_per_student[nombre][1].append(mensaje)
                    stats_per_pair[pareja_actual][1].append(mensaje)
                    frases_del_mensaje.append(mensaje)

            if "?" in mensaje:
                if mensaje.index("?") != len(mensaje) - 1:
                    frase = mensaje.split("? ")
                    for f in frase:
                        if frase.index(f) != len(frase) - 1:
                            frases.append(f + "?")
                            stats_per_student[nombre][1].append(f + "?")
                            stats_per_pair[pareja_actual][1].append(f + "?")
                            frases_del_mensaje.append(f + "?")
                        else:
                            frases.append(f)
                            stats_per_student[nombre][1].append(f)
                            stats_per_pair[pareja_actual][1].append(f)
                            frases_del_mensaje.append(f)
                elif "!" not in mensaje:
                    frases.append(mensaje)
                    stats_per_student[nombre][1].append(mensaje)
                    stats_per_pair[pareja_actual][1].append(mensaje)
                    frases_del_mensaje.append(mensaje)

            if "." in mensaje and "..." not in mensaje:
                if mensaje.index(".") != len(mensaje) - 1:
                    frase = mensaje.split(". ")
                    for f in frase:
                        if frase.index(f) != len(frase) - 1:
                            frases.append(f + ".")
                            stats_per_student[nombre][1].append(f + ".")
                            stats_per_pair[pareja_actual][1].append(f + ".")
                            frases_del_mensaje.append(f + ".")
                        else:
                            frases.append(f)
                            stats_per_student[nombre][1].append(f)
                            stats_per_pair[pareja_actual][1].append(f)
                            frases_del_mensaje.append(f)
                elif "!" not in mensaje and "?" not in mensaje:
                    frases.append(mensaje)
                    stats_per_student[nombre][1].append(mensaje)
                    stats_per_pair[pareja_actual][1].append(mensaje)
                    frases_del_mensaje.append(mensaje)

            if "!" not in mensaje and "?" not in mensaje and "." not in mensaje:
                frases.append(mensaje)
                stats_per_student[nombre][1].append(mensaje)
                stats_per_pair[pareja_actual][1].append(mensaje)
                frases_del_mensaje.append(mensaje)

            for frase in frases_del_mensaje:
                if len(frase.split()) == 1 or (len(frase.split()) == 2 and ('?' in frase or '!' in frase)):
                    frases_una_palabra.append(frase)
                    stats_per_student[nombre][35].append(frase)
                    stats_per_pair[pareja_actual][35].append(frase)

                if '?' in frase:
                    frases_interrogativas.append(frase)
                    stats_per_student[nombre][36].append(frase)
                    stats_per_pair[pareja_actual][36].append(frase)

                if '!' in frase:
                    frases_exclamativas.append(frase)
                    stats_per_student[nombre][37].append(frase)
                    stats_per_pair[pareja_actual][37].append(frase)

            # Turnos
            if '-' in linea_anterior:
                numero_turnos += 1
                stats_per_student[nombre][2][1] += 1
                stats_per_pair[pareja_actual][2][1] += 1
            else:
                nombre_alumno = (linea_dividida[2] + " " + linea_dividida[3]).rstrip(":")
                nombre_alumno_anterior = (linea_anterior_dividida[2] + " " + linea_anterior_dividida[3]).rstrip(":")
                if not nombre_alumno == nombre_alumno_anterior:
                    numero_turnos += 1
                    stats_per_student[nombre_alumno][2][1] += 1
                    stats_per_pair[pareja_actual][2][1] += 1
            linea_anterior = line

            # Diccionario
            lista_palabras = mensaje.split()
            for palabra in lista_palabras:
                if palabra not in caracteres_especiales:
                    # Palabras
                    palabras.append(palabra)
                    if palabra not in palabras_distintas:
                        palabras_distintas.append(palabra)

                    stats_per_student[nombre][3].append(palabra)
                    if palabra not in stats_per_student[nombre][6]:
                        stats_per_student[nombre][6].append(palabra)

                    stats_per_pair[pareja_actual][3].append(palabra)
                    if palabra not in stats_per_pair[pareja_actual][6]:
                        stats_per_pair[pareja_actual][6].append(palabra)

                    # Palabras correctas/incorrectas
                    if d.check(palabra) or palabra.lower() in ampliacion_diccionario or palabra.capitalize() in ampliacion_diccionario:
                        palabras_en_diccionario.append(palabra)
                        if palabra not in palabras_en_diccionario_distintas:
                            palabras_en_diccionario_distintas.append(palabra)

                        stats_per_student[nombre][4].append(palabra)
                        if palabra not in stats_per_student[nombre][7]:
                            stats_per_student[nombre][7].append(palabra)

                        stats_per_pair[pareja_actual][4].append(palabra)
                        if palabra not in stats_per_pair[pareja_actual][7]:
                            stats_per_pair[pareja_actual][7].append(palabra)
                    else:
                        palabras_fuera_diccionario.append(palabra)
                        if palabra not in palabras_fuera_diccionario_distintas:
                            palabras_fuera_diccionario_distintas.append(palabra)

                        stats_per_student[nombre][5].append(palabra)
                        if palabra not in stats_per_student[nombre][8]:
                            stats_per_student[nombre][8].append(palabra)

                        stats_per_pair[pareja_actual][5].append(palabra)
                        if palabra not in stats_per_pair[pareja_actual][8]:
                            stats_per_pair[pareja_actual][8].append(palabra)

            # Palabras reservadas
            expresiones_en_mensaje = usaExpresionReservada(mensaje)
            if len(expresiones_en_mensaje) >= 1:
                for expresion in expresiones_en_mensaje:
                    palabras_reservadas_total.append(expresion)
                    if expresion not in palabras_reservadas_distintas:
                        palabras_reservadas_distintas.append(expresion)

                    stats_per_student[nombre][9].append(expresion)
                    if expresion not in stats_per_student[nombre][22]:
                        stats_per_student[nombre][22].append(expresion)

                    stats_per_pair[pareja_actual][9].append(expresion)
                    if expresion not in stats_per_pair[pareja_actual][22]:
                        stats_per_pair[pareja_actual][22].append(expresion)

                    tipo_expresion = expresion[0]

                    if tipo_expresion == "Pronombre interrogativo":
                        palabras_reservadas_catPronombresInterrogativos.append(expresion)
                        if expresion not in palabras_reservadas_catPronombresInterrogativos_distintas:
                            palabras_reservadas_catPronombresInterrogativos_distintas.append(expresion)

                        stats_per_student[nombre][10].append(expresion)
                        if expresion not in stats_per_student[nombre][23]:
                            stats_per_student[nombre][23].append(expresion)

                        stats_per_pair[pareja_actual][10].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][23]:
                            stats_per_pair[pareja_actual][23].append(expresion)

                    elif tipo_expresion == "Adjetivo":
                        palabras_reservadas_catAdjetivos.append(expresion)
                        if expresion not in palabras_reservadas_catAdjetivos_distintas:
                            palabras_reservadas_catAdjetivos_distintas.append(expresion)

                        stats_per_student[nombre][11].append(expresion)
                        if expresion not in stats_per_student[nombre][24]:
                            stats_per_student[nombre][24].append(expresion)

                        stats_per_pair[pareja_actual][9].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][22]:
                            stats_per_pair[pareja_actual][22].append(expresion)

                    elif tipo_expresion == "Saludo o despedida":
                        palabras_reservadas_catSaludosDespedidas.append(expresion)
                        if expresion not in palabras_reservadas_catSaludosDespedidas_distintas:
                            palabras_reservadas_catSaludosDespedidas_distintas.append(expresion)

                        stats_per_student[nombre][12].append(expresion)
                        if expresion not in stats_per_student[nombre][25]:
                            stats_per_student[nombre][25].append(expresion)

                        stats_per_pair[pareja_actual][12].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][25]:
                            stats_per_pair[pareja_actual][25].append(expresion)

                    elif tipo_expresion == "Frase hecha":
                        palabras_reservadas_catFrasesHechas.append(expresion)
                        if expresion not in palabras_reservadas_catFrasesHechas_distintas:
                            palabras_reservadas_catFrasesHechas_distintas.append(expresion)

                        stats_per_student[nombre][13].append(expresion)
                        if expresion not in stats_per_student[nombre][26]:
                            stats_per_student[nombre][26].append(expresion)

                        stats_per_pair[pareja_actual][13].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][26]:
                            stats_per_pair[pareja_actual][26].append(expresion)

                    elif tipo_expresion == "Expresion de afirmacion":
                        palabras_reservadas_catExpresionesAfirmacion.append(expresion)
                        if expresion not in palabras_reservadas_catExpresionesAfirmacion_distintas:
                            palabras_reservadas_catExpresionesAfirmacion_distintas.append(expresion)

                        stats_per_student[nombre][14].append(expresion)
                        if expresion not in stats_per_student[nombre][27]:
                            stats_per_student[nombre][27].append(expresion)

                        stats_per_pair[pareja_actual][14].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][27]:
                            stats_per_pair[pareja_actual][27].append(expresion)

                    elif tipo_expresion == "Expresion de negacion o duda":
                        palabras_reservadas_catExpresionesNegacionDuda.append(expresion)
                        if expresion not in palabras_reservadas_catExpresionesNegacionDuda_distintas:
                            palabras_reservadas_catExpresionesNegacionDuda_distintas.append(expresion)

                        stats_per_student[nombre][15].append(expresion)
                        if expresion not in stats_per_student[nombre][28]:
                            stats_per_student[nombre][28].append(expresion)

                        stats_per_pair[pareja_actual][15].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][28]:
                            stats_per_pair[pareja_actual][28].append(expresion)

                    elif tipo_expresion == "Lugar":
                        palabras_reservadas_catLugares.append(expresion)
                        if expresion not in palabras_reservadas_catLugares_distintas:
                            palabras_reservadas_catLugares_distintas.append(expresion)

                        stats_per_student[nombre][16].append(expresion)
                        if expresion not in stats_per_student[nombre][29]:
                            stats_per_student[nombre][29].append(expresion)

                        stats_per_pair[pareja_actual][16].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][29]:
                            stats_per_pair[pareja_actual][29].append(expresion)

                    elif tipo_expresion == "Dia de la semana":
                        palabras_reservadas_catDiasSemana.append(expresion)
                        if expresion not in palabras_reservadas_catDiasSemana_distintas:
                            palabras_reservadas_catDiasSemana_distintas.append(expresion)

                        stats_per_student[nombre][17].append(expresion)
                        if expresion not in stats_per_student[nombre][30]:
                            stats_per_student[nombre][30].append(expresion)

                        stats_per_pair[pareja_actual][17].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][30]:
                            stats_per_pair[pareja_actual][30].append(expresion)

                    elif tipo_expresion == "Adverbio temporal":
                        palabras_reservadas_catAdverbiosTemporales.append(expresion)
                        if expresion not in palabras_reservadas_catAdverbiosTemporales_distintas:
                            palabras_reservadas_catAdverbiosTemporales_distintas.append(expresion)

                        stats_per_student[nombre][18].append(expresion)
                        if expresion not in stats_per_student[nombre][31]:
                            stats_per_student[nombre][31].append(expresion)

                        stats_per_pair[pareja_actual][18].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][31]:
                            stats_per_pair[pareja_actual][31].append(expresion)

                    elif tipo_expresion == "Hora":
                        palabras_reservadas_catHoras.append(expresion)
                        if expresion not in palabras_reservadas_catHoras_distintas:
                            palabras_reservadas_catHoras_distintas.append(expresion)

                        stats_per_student[nombre][19].append(expresion)
                        if expresion not in stats_per_student[nombre][32]:
                            stats_per_student[nombre][32].append(expresion)

                        stats_per_pair[pareja_actual][19].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][32]:
                            stats_per_pair[pareja_actual][32].append(expresion)

                    elif tipo_expresion == "Preposicion mit":
                        palabras_reservadas_catMit.append(expresion)
                        if expresion not in palabras_reservadas_catMit_distintas:
                            palabras_reservadas_catMit_distintas.append(expresion)

                        stats_per_student[nombre][20].append(expresion)
                        if expresion not in stats_per_student[nombre][33]:
                            stats_per_student[nombre][33].append(expresion)

                        stats_per_pair[pareja_actual][20].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][33]:
                            stats_per_pair[pareja_actual][33].append(expresion)

                    elif tipo_expresion == "Preposicion con pronombre personal":
                        palabras_reservadas_catPronombresPersonales.append(expresion)
                        if expresion not in palabras_reservadas_catPronombresPersonales_distintas:
                            palabras_reservadas_catPronombresPersonales_distintas.append(expresion)

                        stats_per_student[nombre][21].append(expresion)
                        if expresion not in stats_per_student[nombre][34]:
                            stats_per_student[nombre][34].append(expresion)

                        stats_per_pair[pareja_actual][21].append(expresion)
                        if expresion not in stats_per_pair[pareja_actual][34]:
                            stats_per_pair[pareja_actual][34].append(expresion)

                    else:
                        print "Esto es más raro que la historia de Manuel Bartual..."


# Extracción de actividades en grupo
nombre_act = ""
autor = ""
partners = ""
position = ""
what_exactly = ""
where = ""
where_exactly = ""
trio = True
actividades = []
insertar_actividad = False

for lines in lineas_actividades_grupo:
    for line in lines:
        if insertar_actividad:
            actividad = Actividad(nombre_act, autor, partners, position, what_exactly, where, where_exactly, trio)
            actividades.append(actividad)
            insertar_actividad = False

        if "------------" in line:
            nombre_act = line.split()[1]
        elif "----->" in line:
            autor = line.split()[1] + " " + line.split()[2]
        elif "Partners:" in line:
            if len(line.split()) > 4:
                partners = line.split()[1] + " " + line.split()[2] + "-" + line.split()[4] + " " + line.split()[5]
                trio = True
            else:
                partners = line.split()[1] + " " + line.split()[2]
                trio = False
        elif "Position:" in line:
            position = line.replace("Position: ", "")
        elif "What exactly:" in line:
            what_exactly = line.replace("What exactly: ", "")
        elif "Where:" in line:
            where = line.replace("Where: ", "")
        elif "Where exactly:" in line:
            where_exactly = line.replace("Where exactly: ", "")
            insertar_actividad = True


for actividad in actividades:
    i = 0
    acordando_actividad = False
    index = actividades.index(actividad)
    nombre_act = actividad.nombre_act

    if not actividad.trio:
        while i < len(actividades):
            if nombre_act == actividades[i].nombre_act:
                if i != index and not actividades[i].trio:
                    if actividad.autor == actividades[i].partners and \
                            actividad.partners == actividades[i].autor:
                                acordando_actividad = True
                                alumno1 = actividad.autor
                                alumno2 = actividades[i].autor
                                pareja = alumno1 + "-" + alumno2
                                if pareja not in stats_per_pair.keys():
                                    pareja = alumno2 + "-" + alumno1

                                if actividad.position == actividades[i].position and \
                                    actividad.what_exactly == actividades[i].what_exactly and \
                                    actividad.where == actividades[i].where and \
                                        actividad.where_exactly == actividades[i].where_exactly:
                                            actividades_acordadas_pareja.append(actividad)
                                            stats_per_student[alumno1][59].append(actividad)
                                            stats_per_pair[pareja][59].append(actividad)

                                else:
                                    actividades_mal_acordadas_pareja.append(actividad)
                                    stats_per_student[alumno1][60].append(actividad)
                                    stats_per_pair[pareja][60].append(actividad)
            i += 1

        if not acordando_actividad:
            alumno1 = actividad.autor
            alumno2 = actividad.partners
            pareja = alumno1 + "-" + alumno2
            if pareja not in stats_per_pair.keys():
                pareja = alumno2 + "-" + alumno1

            actividades_propuestas_pareja.append(actividad)
            stats_per_student[alumno1][58].append(actividad)
            stats_per_pair[pareja][58].append(actividad)

    else:
        j = 0
        while i < len(actividades):
            if nombre_act == actividades[i].nombre_act:
                if i != index and actividades[i].trio:
                    if actividad.autor in actividades[i].partners and \
                            actividades[i].autor in actividad.partners:
                                if actividades[i].partners.split("-")[0] != actividades[i].partners.split("-")[1]:
                                    while j < len(actividades):
                                        if nombre_act == actividades[j].nombre_act:
                                            if j != index and actividades[j].trio:
                                                if actividad.autor in actividades[j].partners and \
                                                        actividades[i].autor in actividades[j].partners:
                                                            acordando_actividad = True
                                                            alumno1 = actividad.autor
                                                            alumno2 = actividades[i].autor
                                                            alumno3 = actividades[j].autor
                                                            trio = [alumno1, alumno2, alumno3]
                                                            trio_string = ""

                                                            for comb in list(itertools.permutations(trio)):
                                                                trio_string = comb[0] + "-" + comb[1] + "-" + comb[2]
                                                                if trio_string in actividades_por_trios.keys():
                                                                    break

                                                            if actividad.position == actividades[i].position == actividades[j].position and \
                                                                actividad.what_exactly == actividades[i].what_exactly == actividades[j].what_exactly and \
                                                                actividad.where == actividades[i].where == actividades[j].where and \
                                                                    actividad.where_exactly == actividades[i].where_exactly == actividades[j].where_exactly:
                                                                        actividades_acordadas_trio.append(actividad)
                                                                        stats_per_student[alumno1][62].append(actividad)
                                                                        actividades_por_trios[trio_string][1].append(actividad)

                                                            else:
                                                                actividades_mal_acordadas_trio.append(actividad)
                                                                stats_per_student[alumno1][63].append(actividad)
                                                                actividades_por_trios[trio_string][2].append(actividad)
                                        j += 1
                                else:
                                    if actividad.partners.split("-")[0] == actividad.partners.split("-")[1]:
                                        acordando_actividad = True
                                        alumno1 = actividad.autor
                                        alumno2 = actividad.partners.split("-")[0]
                                        trio = [alumno1, alumno2, alumno2]
                                        trio_string = ""

                                        for comb in list(itertools.permutations(trio)):
                                            trio_string = comb[0] + "-" + comb[1] + "-" + comb[2]
                                            if trio_string in actividades_por_trios.keys():
                                                break

                                        if actividad.position == actividades[i].position and \
                                            actividad.what_exactly == actividades[i].what_exactly and \
                                            actividad.where == actividades[i].where and \
                                                actividad.where_exactly == actividades[i].where_exactly:
                                                    actividades_acordadas_trio.append(actividad)
                                                    stats_per_student[alumno1][62].append(actividad)
                                                    actividades_por_trios[trio_string][1].append(actividad)

                                        else:
                                            actividades_mal_acordadas_trio.append(actividad)
                                            stats_per_student[alumno1][63].append(actividad)
                                            actividades_por_trios[trio_string][2].append(actividad)
            i += 1

        if not acordando_actividad:
            alumno1 = actividad.autor
            alumno2 = actividad.partners.split("-")[0]
            alumno3 = actividad.partners.split("-")[1]
            trio = [alumno1, alumno2, alumno3]
            trio_string = ""

            for comb in list(itertools.permutations(trio)):
                trio_string = comb[0] + "-" + comb[1] + "-" + comb[2]
                if trio_string in actividades_por_trios.keys():
                    break

            actividades_propuestas_trio.append(actividad)
            stats_per_student[alumno1][61].append(actividad)
            actividades_por_trios[trio_string][0].append(actividad)

# Extracción de actividades individuales
nombre_act = ""
autor = ""
partners = ""
position = ""
what_exactly = ""
where = ""
where_exactly = ""
trio = False
actividades_individuales = []
insertar_actividad = False

for lines in lineas_actividades_individuales:
    for line in lines:
        if insertar_actividad:
            actividad = Actividad(nombre_act, autor, partners, position, what_exactly, where, where_exactly, trio)
            actividades_individuales.append(actividad)
            insertar_actividad = False

        if "------------" in line:
            nombre_act = "Individuelle Aktivitäten"
        elif "----->" in line:
            autor = line.split()[1] + " " + line.split()[2]
        elif "Position:" in line:
            position = line.replace("Position: ", "")
        elif "What exactly:" in line:
            what_exactly = line.replace("What exactly: ", "")
        elif "Where:" in line:
            where = line.replace("Where: ", "")
        elif "Where exactly:" in line:
            where_exactly = line.replace("Where exactly: ", "")
            insertar_actividad = True

for actividad in actividades_individuales:
    actividades_acordadas_individuales.append(actividad)
    stats_per_student[actividad.autor][64].append(actividad)

