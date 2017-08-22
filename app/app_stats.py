#!/usr/bin/env python
# encoding: utf-8

""" Script para buscar estadísticas en los logs de la aplicación TerminKalender.
    Visita la documentación para obtener información más detallada.

    Autor: Luis Gonzaga Rozo Bueno. 2017.
"""

from datetime import time, datetime, timedelta

import enchant
import os
import re

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

# for log in logs:
#     for line in log:
#         print line

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

fichero_con_tareas = open(r'../tasks.xml', 'r').readlines()
for linea in fichero_con_tareas:
    if '<field>' in linea:
        palabras = re.sub(r'<field>|\(|\)|</field>', '', linea).split()
        for palabra in palabras:
            ampliacion_diccionario.append(palabra.title())
            ampliacion_diccionario.append(palabra.lower())

for palabra in lista_manual:
    ampliacion_diccionario.append(palabra)

for adv in adverbios_temporales:
    ampliacion_diccionario.append(adv)

ampliacion_diccionario = sorted(set(ampliacion_diccionario))

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

stats_per_student = {}
stats_per_pair = {}

# Este vector se utiliza para almacenar las estadisticas por estudiante y por pareja.
# Para ello, se le asigna dicho vector a cada entrada del diccionario, respondiendo a los siguientes indices:
# 0: Mensajes
# 1: Turnos en unidades
# 2: Frases
# ...

for alumno in alumnos:
    stats_per_student[alumno] = [["Mensajes"], ["Turnos (unidades)"], ["Frases"], ]

for pareja in parejas:
    stats_per_pair[pareja] = [["Mensajes"], ["Turnos (unidades)"], ["Frases"], ]

""" Estadísticas generales """
# Obtención de mensajes, turnos y frases
mensajes = []
frases = []
linea_anterior = '-'
numero_turnos = 0
tiempo_turnos = []
i = 0

for log in logs:
    for line in log:
        if line.startswith(":", 2, 3):
            linea_dividida = line.split()
            linea_anterior_dividida = linea_anterior.split()

            mensaje = ' '.join(linea_dividida[4:])
            mensajes.append(mensaje)
            nombre = (linea_dividida[2] + " " + linea_dividida[3]).rstrip(":")

            stats_per_student[nombre][0].append(mensaje)

            if '-' in linea_anterior:
                numero_turnos += 1
            else:
                nombre_alumno = (linea_dividida[2] + " " + linea_dividida[3]).rstrip(":")
                nombre_alumno_anterior = (linea_anterior_dividida[2] + " " + linea_anterior_dividida[3]).rstrip(":")
                if not nombre_alumno == nombre_alumno_anterior:
                    numero_turnos += 1
            linea_anterior = line

for mensaje in stats_per_student["Reyes Rosales"][0]:
    print mensaje

for mensaje in mensajes:
    if "!" in mensaje:
        if mensaje.index("!") != len(mensaje) - 1:
            frase = mensaje.split("! ")
            for f in frase:
                if frase.index(f) != len(frase)-1:
                    frases.append(f+"!")
                else:
                    frases.append(f)
        else:
            frases.append(mensaje)

    if "?" in mensaje:
        if mensaje.index("?") != len(mensaje) - 1:
            frase = mensaje.split("? ")
            for f in frase:
                if frase.index(f) != len(frase)-1:
                    frases.append(f+"?")
                else:
                    frases.append(f)
        elif "!" not in mensaje:
            frases.append(mensaje)

    if "." in mensaje and "..." not in mensaje:
        if mensaje.index(".") != len(mensaje) - 1:
            frase = mensaje.split(". ")
            for f in frase:
                if frase.index(f) != len(frase)-1:
                    frases.append(f+".")
                else:
                    frases.append(f)
        elif "!" not in mensaje and "?" not in mensaje:
            frases.append(mensaje)

    if "!" not in mensaje and "?" not in mensaje and "." not in mensaje:
        frases.append(mensaje)

# Palabras y corrección según diccionario
palabras = []
palabras_en_diccionario = []
palabras_fuera_diccionario = []

caracteres_especiales = ["?", "!", ",", ".", "#", "*", "O.o", "(", ")"]
d = enchant.Dict("de_DE")

for mensaje in mensajes:
    lista_palabras = mensaje.split()
    for palabra in lista_palabras:
        if palabra not in caracteres_especiales:
            palabras.append(palabra)

            if d.check(palabra) or palabra.lower() in ampliacion_diccionario or palabra.capitalize() in ampliacion_diccionario:
                palabras_en_diccionario.append(palabra)
            else:
                palabras_fuera_diccionario.append(palabra)


palabras = sorted(palabras)
palabras_distintas = list(set(palabras))
palabras_en_diccionario = sorted(palabras_en_diccionario)
palabras_fuera_diccionario = sorted(palabras_fuera_diccionario)
palabras_en_diccionario_distintas = sorted(set(palabras_en_diccionario))
palabras_fuera_diccionario_distintas = sorted(set(palabras_fuera_diccionario))

# print len(mensajes)
# print len(frases)
# print len(palabras)
# print len(palabras_en_diccionario)
# print len(palabras_fuera_diccionario)
# print len(palabras_distintas)
# print len(palabras_en_diccionario_distintas)
# print len(palabras_fuera_diccionario_distintas)

# Palabras o expresiones reservadas
'''palabras_reservadas_total = []
palabras_reservadas_distintas = []
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

for frase in frases:
    expresiones_en_frase = usaExpresionReservada(frase)
    if len(expresiones_en_frase) >= 1:
        for expresion in expresiones_en_frase:
            palabras_reservadas_total.append(expresion)
            if expresion not in palabras_reservadas_distintas:
                palabras_reservadas_distintas.append(expresion)

num_palabras_reservadas_total = len(palabras_reservadas_total)
num_palabras_reservadas_distintas = len(palabras_reservadas_distintas)

for expresion in palabras_reservadas_total:
    tipo_expresion = expresion[0]
    if tipo_expresion == "Pronombre interrogativo":
        palabras_reservadas_catPronombresInterrogativos.append(expresion)
        if expresion not in palabras_reservadas_catPronombresInterrogativos_distintas:
            palabras_reservadas_catPronombresInterrogativos_distintas.append(expresion)
    elif tipo_expresion == "Adjetivo":
        palabras_reservadas_catAdjetivos.append(expresion)
        if expresion not in palabras_reservadas_catAdjetivos_distintas:
            palabras_reservadas_catAdjetivos_distintas.append(expresion)
    elif tipo_expresion == "Saludo o despedida":
        palabras_reservadas_catSaludosDespedidas.append(expresion)
        if expresion not in palabras_reservadas_catSaludosDespedidas_distintas:
            palabras_reservadas_catSaludosDespedidas_distintas.append(expresion)
    elif tipo_expresion == "Frase hecha":
        palabras_reservadas_catFrasesHechas.append(expresion)
        if expresion not in palabras_reservadas_catFrasesHechas_distintas:
            palabras_reservadas_catFrasesHechas_distintas.append(expresion)
    elif tipo_expresion == "Expresion de afirmacion":
        palabras_reservadas_catExpresionesAfirmacion.append(expresion)
        if expresion not in palabras_reservadas_catExpresionesAfirmacion_distintas:
            palabras_reservadas_catExpresionesAfirmacion_distintas.append(expresion)
    elif tipo_expresion == "Expresion de negacion o duda":
        palabras_reservadas_catExpresionesNegacionDuda.append(expresion)
        if expresion not in palabras_reservadas_catExpresionesNegacionDuda_distintas:
            palabras_reservadas_catExpresionesNegacionDuda_distintas.append(expresion)
    elif tipo_expresion == "Lugar":
        palabras_reservadas_catLugares.append(expresion)
        if expresion not in palabras_reservadas_catLugares_distintas:
            palabras_reservadas_catLugares_distintas.append(expresion)
    elif tipo_expresion == "Dia de la semana":
        palabras_reservadas_catDiasSemana.append(expresion)
        if expresion not in palabras_reservadas_catDiasSemana_distintas:
            palabras_reservadas_catDiasSemana_distintas.append(expresion)
    elif tipo_expresion == "Adverbio temporal":
        palabras_reservadas_catAdverbiosTemporales.append(expresion)
        if expresion not in palabras_reservadas_catAdverbiosTemporales_distintas:
            palabras_reservadas_catAdverbiosTemporales_distintas.append(expresion)
    elif tipo_expresion == "Hora":
        palabras_reservadas_catHoras.append(expresion)
        if expresion not in palabras_reservadas_catHoras_distintas:
            palabras_reservadas_catHoras_distintas.append(expresion)
    elif tipo_expresion == "Preposicion mit":
        palabras_reservadas_catMit.append(expresion)
        if expresion not in palabras_reservadas_catMit_distintas:
            palabras_reservadas_catMit_distintas.append(expresion)
    elif tipo_expresion == "Preposicion con pronombre personal":
        palabras_reservadas_catPronombresPersonales.append(expresion)
        if expresion not in palabras_reservadas_catPronombresPersonales_distintas:
            palabras_reservadas_catPronombresPersonales_distintas.append(expresion)
    else:
        print "¿Pero que esta pasando aqui?"


num_palabras_reservadas_catPronombresInterrogativos = len(palabras_reservadas_catPronombresInterrogativos)
num_palabras_reservadas_catAdjetivos = len(palabras_reservadas_catAdjetivos)
num_palabras_reservadas_catSaludosDespedidas = len(palabras_reservadas_catSaludosDespedidas)
num_palabras_reservadas_catFrasesHechas = len(palabras_reservadas_catFrasesHechas)
num_palabras_reservadas_catExpresionesAfirmacion = len(palabras_reservadas_catExpresionesAfirmacion)
num_palabras_reservadas_catExpresionesNegacionDuda = len(palabras_reservadas_catExpresionesNegacionDuda)
num_palabras_reservadas_catLugares = len(palabras_reservadas_catLugares)
num_palabras_reservadas_catDiasSemana = len(palabras_reservadas_catDiasSemana)
num_palabras_reservadas_catAdverbiosTemporales = len(palabras_reservadas_catAdverbiosTemporales)
num_palabras_reservadas_catHoras = len(palabras_reservadas_catHoras)
num_palabras_reservadas_catMit = len(palabras_reservadas_catMit)
num_palabras_reservadas_catPronombresPersonales = len(palabras_reservadas_catPronombresPersonales)
num_palabras_reservadas_catPronombresInterrogativos_distintas = \
    len(palabras_reservadas_catPronombresInterrogativos_distintas)
num_palabras_reservadas_catAdjetivos_distintas = len(palabras_reservadas_catAdjetivos_distintas)
num_palabras_reservadas_catSaludosDespedidas_distintas = len(palabras_reservadas_catSaludosDespedidas_distintas)
num_palabras_reservadas_catFrasesHechas_distintas = len(palabras_reservadas_catFrasesHechas_distintas)
num_palabras_reservadas_catExpresionesAfirmacion_distintas = len(palabras_reservadas_catExpresionesAfirmacion_distintas)
num_palabras_reservadas_catExpresionesNegacionDuda_distintas = \
    len(palabras_reservadas_catExpresionesNegacionDuda_distintas)
num_palabras_reservadas_catLugares_distintas = len(palabras_reservadas_catLugares_distintas)
num_palabras_reservadas_catDiasSemana_distintas = len(palabras_reservadas_catDiasSemana_distintas)
num_palabras_reservadas_catAdverbiosTemporales_distintas = len(palabras_reservadas_catAdverbiosTemporales_distintas)
num_palabras_reservadas_catHoras_distintas = len(palabras_reservadas_catHoras_distintas)
num_palabras_reservadas_catMit_distintas = len(palabras_reservadas_catMit_distintas)
num_palabras_reservadas_catPronombresPersonales_distintas = len(palabras_reservadas_catPronombresPersonales_distintas)

print "-------------"
print "Palabras reservadas total:", num_palabras_reservadas_total, ", de las cuales distintas:", num_palabras_reservadas_distintas
print "-------------"
print "Pronombres interrogativos:", num_palabras_reservadas_catPronombresInterrogativos, ", de los cuales distintos:", num_palabras_reservadas_catPronombresInterrogativos_distintas
for expresion in palabras_reservadas_catPronombresInterrogativos:
    print expresion[1] + ",",
print "\n-------------"
print "Adjetivos:", num_palabras_reservadas_catAdjetivos, ", de los cuales distintos:", num_palabras_reservadas_catAdjetivos_distintas
for expresion in palabras_reservadas_catAdjetivos_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Saludos o despedidas:", num_palabras_reservadas_catSaludosDespedidas, ", de los cuales distintos:", num_palabras_reservadas_catSaludosDespedidas_distintas
for expresion in palabras_reservadas_catSaludosDespedidas_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Frases hechas:", num_palabras_reservadas_catFrasesHechas, ", de los cuales distintos:", num_palabras_reservadas_catFrasesHechas_distintas
for expresion in palabras_reservadas_catFrasesHechas_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Expresiones de afirmacion:", num_palabras_reservadas_catExpresionesAfirmacion, ", de los cuales distintos:", num_palabras_reservadas_catExpresionesAfirmacion_distintas
for expresion in palabras_reservadas_catExpresionesAfirmacion_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Expresiones de negacion o duda:", num_palabras_reservadas_catExpresionesNegacionDuda, ", de los cuales distintos:", num_palabras_reservadas_catExpresionesNegacionDuda_distintas
for expresion in palabras_reservadas_catExpresionesNegacionDuda_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Lugares:", num_palabras_reservadas_catLugares, ", de los cuales distintos:", num_palabras_reservadas_catLugares_distintas
for expresion in palabras_reservadas_catLugares_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Dias de la semana:", num_palabras_reservadas_catDiasSemana, ", de los cuales distintos:", num_palabras_reservadas_catDiasSemana_distintas
for expresion in palabras_reservadas_catDiasSemana:
    print expresion[1] + ",",
print "\n-------------"
print "Adverbios temporales:", num_palabras_reservadas_catAdverbiosTemporales, ", de los cuales distintos:", num_palabras_reservadas_catAdverbiosTemporales_distintas
for expresion in palabras_reservadas_catAdverbiosTemporales_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Horas:", num_palabras_reservadas_catHoras, ", de los cuales distintos:", num_palabras_reservadas_catHoras_distintas
for expresion in palabras_reservadas_catHoras_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Preposicion mit:", num_palabras_reservadas_catMit, ", de los cuales distintos:", num_palabras_reservadas_catMit_distintas
for expresion in palabras_reservadas_catMit_distintas:
    print expresion[1] + ",",
print "\n-------------"
print "Pronombres personales:", num_palabras_reservadas_catPronombresPersonales, ", de los cuales distintos:", num_palabras_reservadas_catPronombresPersonales_distintas
for expresion in palabras_reservadas_catPronombresPersonales_distintas:
    print expresion[1] + ",",
print "\n-------------"'''

