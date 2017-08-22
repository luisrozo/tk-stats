#!/usr/bin/env python
# encoding: utf-8

""" Script para analizar los logs de la aplicación Terminkalender en su versión en papel.
    Visita la documentación para más información: (insertar enlace a github)
    Autor: Luis Gonzaga Rozo Bueno
"""

from openpyxl import load_workbook

import os
import re
import enchant

# Para obtener las estadisticas referentes a palabras o expresiones reservadas, se hace uso de la siguientes estructuras

pronombres_interrogativos = ["mit wem", "um wie viel Uhr", "um wieviel Uhr", "wann", "was", "wer", "wie",
                             "wo", "wohin"]

adjetivos = ["frei", "gestresst", "hungrig", "müde", "happy", "glücklich"]

saludos_despedidas = ["auf Wiedersehen!", "bis Montag", "bis Dienstag",
                      "bis Mittwoch", "bis Donnerstag", "bis Freitag", "bis Samstag", "bis Sonntag",
                      "bis bald", "bis dann", "bis später",
                      "ciao", "hallihallo", "hallo", "hey", "hi", "mach's gut", "tschüs",
                      "tschüs, bis bald", "tschüs, bis dann", "tschüs, bis später", "tschüss", "tschüss, bis bald",
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

expresiones_afirmacion = ["alles klar", "das ist gut", "genial", "gut", "ja, cool", "ja cool", "ja, klar", "ja klar",
                          "ja, klasse", "ja klasse", "ja, natürlich", "ja natürlich", "ja, perfekt", "ja perfekt",
                          "ja, phantastisch", "ja phantastisch", "ja, super Idee", "ja super Idee",
                          "ja, super", "ja super", "ja, wunderbar", "ja wunderbar", "kein Problem", "klasse", "ok",
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
                        "am Mittwochvormittag", "am Mittwochmittag", "am Mittwochnachmittag", "am Mittwochabend",
                        "am Donnerstagmorgen", "am Donnerstagvormittag", "am Donnerstagmittag",
                        "am Donnerstagnachmittag", "am Donnerstagabend", "am Freitagmorgen", "am Freitagvormittag",
                        "am Freitagmittag", "am Freitagnachmittag", "am Freitagabend", "am Samstagmorgen",
                        "am Samstagvormittag", "am Samstagmittag", "am Samstagnachmittag", "am Samstagabend",
                        "am Sonntagmorgen", "am Sonntagvormittag", "am Sonntagmittag", "am Sonntagnachmittag",
                        "am Sonntagabend",
                        "Montagnacht", "Dienstagnacht", "Mittwochnacht", "Donnerstagnacht",
                        "Freitagnacht", "Samstagnacht", "Sonntagnacht",
                        'montagmorgens', 'montagvormittags', 'montagmittags', 'montagnachmittags', 'montagabends',
                        'montagnachts', 'dienstagmorgens', 'dienstagvormittags', 'dienstagmittags',
                        'dienstagnachmittags', 'dienstagabends', 'dienstagnachts', 'mittwochmorgens',
                        'mittwochvormittags', 'mittwochmittags', 'mittwochnachmittags', 'mittwochabends',
                        'mittwochnachts', 'donnerstagmorgens', 'donnerstagvormittags', 'donnerstagmittags',
                        'donnerstagnachmittags', 'donnerstagabends', 'donnerstagnachts', 'freitagmorgens',
                        'freitagvormittags', 'freitagmittags', 'freitagnachmittags', 'freitagabends', 'freitagnachts',
                        'samstagmorgens', 'samstagvormittags', 'samstagmittags', 'samstagnachmittags', 'samstagabends',
                        'samstagnachts', 'sonntagmorgens', 'sonntagvormittags', 'sonntagmittags', 'sonntagnachmittags',
                        'sonntagabends', 'sonntagnachts',
                        "am Vormittag", "am Mittag", "am Nachmittag", "am Abend", "in der Nacht", "am Montag",
                        "am Dienstag", "am Mittwoch", "am Donnerstag", "am Freitag", "am Samstag", "am Sonntag"]

horas = ["um 1 Uhr", "um 2 Uhr", "um 3 Uhr", "um 4 Uhr", "um 5 Uhr", "um 6 Uhr", "um 7 Uhr", "um 8 Uhr",
         "um 9 Uhr", "um 10 Uhr", "um 11 Uhr", "um 12 Uhr", "um 13 Uhr", "um 14 Uhr", "um 15 Uhr", "um 16 Uhr",
         "um 17 Uhr", "um 18 Uhr", "um 19 Uhr", "um 20 Uhr", "um 21 Uhr", "um 22 Uhr", "um 23 Uhr", "um 24 Uhr",
         'um 1', 'um 2', 'um 3', 'um 4', 'um 5', 'um 6', 'um 7', 'um 8', 'um 9', 'um 10', 'um 11', 'um 12', 'um 13',
         'um 14', 'um 15', 'um 16', 'um 17', 'um 18', 'um 19', 'um 20', 'um 21', 'um 22', 'um 23', 'um 24'
         "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
         "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig", "einundzwanzig",
         "zweiundzwanzig", "dreiundzwanzig", "vierundzwanzig",
         'um ein', 'um zwei', 'um drei', 'um vier', 'um fünf', 'um sechs', 'um sieben', 'um acht', 'um neun',
         'um zehn', 'um elf', 'um zwölf', 'um dreizehn', 'um vierzehn', 'um fünfzehn', 'um sechzehn',
         'um siebzehn', 'um achtzehn', 'um neunzehn', 'um zwanzig', 'um einundzwanzig', 'um zweiundzwanzig',
         'um dreiundzwanzig', 'um vierundzwanzig']

preposiciones_con_pronombres_personales = ["mit mir", "mit dir", "mit uns"]


# Si se añaden nuevos tipos de palabras o expresiones reservadas, añadirlo tambien en estas dos estructuras.

tipos_expresiones = ["Pronombre interrogativo", "Adjetivo", "Saludo o despedida", "Frase hecha",
                     "Expresion de afirmacion", "Expresion de negacion o duda", "Lugar", "Dia de la semana",
                     "Adverbio temporal", "Hora", "Preposicion con pronombre personal"]

array_expresiones = [pronombres_interrogativos, adjetivos, saludos_despedidas, frases_hechas,
                     expresiones_afirmacion, expresiones_negacion_duda, lugares, dias_de_la_semana,
                     adverbios_temporales, horas, preposiciones_con_pronombres_personales]


# Para tener en cuenta las mayusculas o minusculas en las busquedas, se hara uso de esta lista de sustantivos:

sustantivos = ["Abend", "Ahnung", "Bibliothek", "Café", "Copycenter", "Copyshop", "Dienstag", "Dienstagnacht", "Disco",
               "Disko", "Diskothek", "Donnerstag", "Donnerstagnacht", "Einkaufszentrum", "Eiscafé", "Fitnessstudio",
               "Fitnesszentrum", "Freitag", "Freitagnacht", "Fussballplatz", "Fußballplatz", "Fussballstadion",
               "Fußballstadion", "Fussballstadium", "Fußballstadium", "Idee", "Kino", "Kneipe", "Konzert", "Mittag",
               "Mittwoch", "Mittwochnacht", "Montag", "Montagnacht", "Nachmittag", "Nacht", "Problem", "Pub",
               "Restaurant", "Samstag", "Samstagnacht", "Schwimmbad", "Sonntag", "Sonntagnacht", "Sportzentrum",
               "Strand", "Supermarkt", "Tennisplatz", "Theater", "Uhr", "Uni", "Universität", "Vormittag", "Wochenende",
               "Zeit", "Zentrum", "zu Hause", "zuhause"]

# Esta ampliación de diccionario contiene palabras que el módulo 'enchant' no
# considera correctas para el diccionario alemán, pero no son incorrectas al tratarse
# de nombres de lugares, actividades, etc., que se utilizan en los chats para concretar
# los planes.
ampliacion_diccionario = []
fichero_con_tareas = open(r'../tasks.xml', 'r').readlines()
for linea in fichero_con_tareas:
    if '<field>' in linea:
        palabras = re.sub(r'<field>|\(|\)|</field>', '', linea).split()
        for palabra in palabras:
            if palabra not in ampliacion_diccionario:
                ampliacion_diccionario.append(palabra)

for adv in adverbios_temporales:
    ampliacion_diccionario.append(adv)

''' Funciones auxiliares '''


def obtener_alumnos(hoja_libro):
    alumnos_hoja = []
    i = 0
    while i < hoja_libro.max_row:
        if data[i][0].font.b and type(data[i][0]) != 'NoneType':
            if data[i][0].value not in alumnos_hoja and data[i][0].value is not None:
                alumnos_hoja.append(data[i][0].value)
        if data[i][1].font.b and type(data[i][1]) != 'NoneType':
            if data[i][1].value not in alumnos_hoja and data[i][1].value is not None:
                alumnos_hoja.append(data[i][1].value)
        i += 1

    return alumnos_hoja


def obtener_frases(maximo_filas):
    frases_hoja = []
    i = 0
    while i < maximo_filas:
        if not data[i][0].font.b and type(data[i][0]) != 'NoneType':
            if data[i][0].value is not None:
                frases_hoja.append(data[i][0].value)
        if not data[i][1].font.b and type(data[i][1]) != 'NoneType':
            if data[i][1].value is not None:
                frases_hoja.append(data[i][1].value)

        i += 1

    # Decodificar frases de Unicode a String
    frases_codificadas = []
    for frase in frases_hoja:
        frases_codificadas.append(frase.encode("utf-8"))

    return frases_codificadas


def usaExpresionReservada(frase):
    # El array expresionesUtilizadas contendra tuplas de la forma [Tipo de expresion, expresion]
    expresionesUtilizadas = []
    # La variable 'i' ayuda a obtener el tipo de la expresion que se ha detectado
    i = 0
    for tipo_expresion in array_expresiones:
        for expresion in tipo_expresion:
            sustantivos_utilizados = []
            busqueda_refinada = False

            # Determinamos si hacer busqueda refinada, y guardamos los sustantivos utilizados en la frase.
            for sustantivo in sustantivos:
                sustantivo_encontrado = re.findall(r'\b'+sustantivo+r'\b', frase)
                if sustantivo_encontrado:
                    sustantivos_utilizados.append(sustantivo)
                    busqueda_refinada = True

            # Se pasa la frase a minusuculas, dejando solamente los sustantivos en mayuscula.
            if busqueda_refinada:
                frase = frase.lower()
                for sustantivo in sustantivos_utilizados:
                    sustitucion = re.findall(r'\b'+sustantivo+r'\b', frase, re.IGNORECASE)
                    frase = frase.replace(sustitucion[0], sustantivo)
                if expresion in frase:
                    expresionesUtilizadas.append([tipos_expresiones[i], expresion])

            # Se compara con la frase original o con la frase en minusculas.
            else:
                if expresion in frase or expresion in frase.lower():
                    expresionesUtilizadas.append([tipos_expresiones[i], expresion])
        i += 1

    return expresionesUtilizadas

alumnos = []
ficheros = []

# Abrimos todas las hojas de cálculo en las que se van a buscar las estadísticas
for fichero in os.listdir("."):
    if ".xlsx" in fichero and "#" not in fichero:
        ficheros.append(fichero)

for fichero in ficheros:
    prueba = load_workbook(fichero)

    # palabras_reservadas_total = []
    # palabras_reservadas_distintas = []
    # palabras_reservadas_catPronombresInterrogativos = []
    # palabras_reservadas_catAdjetivos = []
    # palabras_reservadas_catSaludosDespedidas = []
    # palabras_reservadas_catFrasesHechas = []
    # palabras_reservadas_catExpresionesAfirmacion = []
    # palabras_reservadas_catExpresionesNegacionDuda = []
    # palabras_reservadas_catLugares = []
    # palabras_reservadas_catDiasSemana = []
    # palabras_reservadas_catAdverbiosTemporales = []
    # palabras_reservadas_catHoras = []
    # palabras_reservadas_catPronombresPersonales = []
    # palabras_reservadas_catPronombresInterrogativos_distintas = []
    # palabras_reservadas_catAdjetivos_distintas = []
    # palabras_reservadas_catSaludosDespedidas_distintas = []
    # palabras_reservadas_catFrasesHechas_distintas = []
    # palabras_reservadas_catExpresionesAfirmacion_distintas = []
    # palabras_reservadas_catExpresionesNegacionDuda_distintas = []
    # palabras_reservadas_catLugares_distintas = []
    # palabras_reservadas_catDiasSemana_distintas = []
    # palabras_reservadas_catAdverbiosTemporales_distintas = []
    # palabras_reservadas_catHoras_distintas = []
    # palabras_reservadas_catPronombresPersonales_distintas = []

    for hoja in prueba:
        inicio = 'A1'
        fin = 'B' + str(hoja.max_row)
        intervalo = inicio + ':' + fin
        data = hoja[intervalo]

        # Frases
        maximo_filas = hoja.max_row
        frases = obtener_frases(maximo_filas)

        # Obtención de alumnos
        alumnos += obtener_alumnos(hoja)

    # Palabras y corrección según diccicd onario
    palabras = []
    palabras_distintas = []
    palabras_en_diccionario = []
    palabras_en_diccionario_distintas = []
    palabras_fuera_diccionario = []
    palabras_fuera_diccionario_distintas = []

    caracteres_especiales = ["?", "!", ",", ".", "#", "*", "O.o", "(", ")"]
    d = enchant.Dict("de_DE")

    for mensaje in frases:
        lista_palabras = mensaje.split()
        for palabra in lista_palabras:
            if palabra not in caracteres_especiales:
                palabras.append(palabra)
                if palabra not in palabras_distintas:
                    palabras_distintas.append(palabra)

                if d.check(
                        palabra) or palabra.lower() in ampliacion_diccionario or palabra.capitalize() in ampliacion_diccionario:
                    palabras_en_diccionario.append(palabra)
                    if palabra not in palabras_en_diccionario_distintas:
                        palabras_en_diccionario_distintas.append(palabra)
                else:
                    palabras_fuera_diccionario.append(palabra)
                    if palabra not in palabras_fuera_diccionario_distintas:
                        palabras_fuera_diccionario_distintas.append(palabra)

    # print len(mensajes)
    print len(frases)
    print len(palabras)
    print len(palabras_en_diccionario)
    print len(palabras_fuera_diccionario)
    print len(palabras_distintas)
    print len(palabras_en_diccionario_distintas)
    print len(palabras_fuera_diccionario_distintas)

    # alumnos = sorted(set(alumnos))
    # for alumno in alumnos:
    #     print alumno

        # for frase in frases:
        #     # print frase
        #     expresiones_en_frase = usaExpresionReservada(frase)
        #     if len(expresiones_en_frase) >= 1:
        #         for expresion in expresiones_en_frase:
        #             palabras_reservadas_total.append(expresion)
        #             if expresion not in palabras_reservadas_distintas:
        #                 palabras_reservadas_distintas.append(expresion)
        #
        # for expresion in palabras_reservadas_total:
        #     tipo_expresion = expresion[0]
        #     if tipo_expresion == "Pronombre interrogativo":
        #         palabras_reservadas_catPronombresInterrogativos.append(expresion)
        #         if expresion not in palabras_reservadas_catPronombresInterrogativos_distintas:
        #             palabras_reservadas_catPronombresInterrogativos_distintas.append(expresion)
        #     elif tipo_expresion == "Adjetivo":
        #         palabras_reservadas_catAdjetivos.append(expresion)
        #         if expresion not in palabras_reservadas_catAdjetivos_distintas:
        #             palabras_reservadas_catAdjetivos_distintas.append(expresion)
        #     elif tipo_expresion == "Saludo o despedida":
        #         palabras_reservadas_catSaludosDespedidas.append(expresion)
        #         if expresion not in palabras_reservadas_catSaludosDespedidas_distintas:
        #             palabras_reservadas_catSaludosDespedidas_distintas.append(expresion)
        #     elif tipo_expresion == "Frase hecha":
        #         palabras_reservadas_catFrasesHechas.append(expresion)
        #         if expresion not in palabras_reservadas_catFrasesHechas_distintas:
        #             palabras_reservadas_catFrasesHechas_distintas.append(expresion)
        #     elif tipo_expresion == "Expresion de afirmacion":
        #         palabras_reservadas_catExpresionesAfirmacion.append(expresion)
        #         if expresion not in palabras_reservadas_catExpresionesAfirmacion_distintas:
        #             palabras_reservadas_catExpresionesAfirmacion_distintas.append(expresion)
        #     elif tipo_expresion == "Expresion de negacion o duda":
        #         palabras_reservadas_catExpresionesNegacionDuda.append(expresion)
        #         if expresion not in palabras_reservadas_catExpresionesNegacionDuda_distintas:
        #             palabras_reservadas_catExpresionesNegacionDuda_distintas.append(expresion)
        #     elif tipo_expresion == "Lugar":
        #         palabras_reservadas_catLugares.append(expresion)
        #         if expresion not in palabras_reservadas_catLugares_distintas:
        #             palabras_reservadas_catLugares_distintas.append(expresion)
        #     elif tipo_expresion == "Dia de la semana":
        #         palabras_reservadas_catDiasSemana.append(expresion)
        #         if expresion not in palabras_reservadas_catDiasSemana_distintas:
        #             palabras_reservadas_catDiasSemana_distintas.append(expresion)
        #     elif tipo_expresion == "Adverbio temporal":
        #         palabras_reservadas_catAdverbiosTemporales.append(expresion)
        #         if expresion not in palabras_reservadas_catAdverbiosTemporales_distintas:
        #             palabras_reservadas_catAdverbiosTemporales_distintas.append(expresion)
        #     elif tipo_expresion == "Hora":
        #         palabras_reservadas_catHoras.append(expresion)
        #         if expresion not in palabras_reservadas_catHoras_distintas:
        #             palabras_reservadas_catHoras_distintas.append(expresion)
        #     elif tipo_expresion == "Preposicion con pronombre personal":
        #         palabras_reservadas_catPronombresPersonales.append(expresion)
        #         if expresion not in palabras_reservadas_catPronombresPersonales_distintas:
        #             palabras_reservadas_catPronombresPersonales_distintas.append(expresion)
        #     else:
        #         print "¿Pero que esta pasando aqui, iho? -_-"


    # num_palabras_reservadas_total = len(palabras_reservadas_total)
    # num_palabras_reservadas_distintas = len(palabras_reservadas_distintas)
    #
    # num_palabras_reservadas_catPronombresInterrogativos = len(palabras_reservadas_catPronombresInterrogativos)
    # num_palabras_reservadas_catAdjetivos = len(palabras_reservadas_catAdjetivos)
    # num_palabras_reservadas_catSaludosDespedidas = len(palabras_reservadas_catSaludosDespedidas)
    # num_palabras_reservadas_catFrasesHechas = len(palabras_reservadas_catFrasesHechas)
    # num_palabras_reservadas_catExpresionesAfirmacion = len(palabras_reservadas_catExpresionesAfirmacion)
    # num_palabras_reservadas_catExpresionesNegacionDuda = len(palabras_reservadas_catExpresionesNegacionDuda)
    # num_palabras_reservadas_catLugares = len(palabras_reservadas_catLugares)
    # num_palabras_reservadas_catDiasSemana = len(palabras_reservadas_catDiasSemana)
    # num_palabras_reservadas_catAdverbiosTemporales = len(palabras_reservadas_catAdverbiosTemporales)
    # num_palabras_reservadas_catHoras = len(palabras_reservadas_catHoras)
    # num_palabras_reservadas_catPronombresPersonales = len(palabras_reservadas_catPronombresPersonales)
    # num_palabras_reservadas_catPronombresInterrogativos_distintas = \
    #     len(palabras_reservadas_catPronombresInterrogativos_distintas)
    # num_palabras_reservadas_catAdjetivos_distintas = len(palabras_reservadas_catAdjetivos_distintas)
    # num_palabras_reservadas_catSaludosDespedidas_distintas = len(palabras_reservadas_catSaludosDespedidas_distintas)
    # num_palabras_reservadas_catFrasesHechas_distintas = len(palabras_reservadas_catFrasesHechas_distintas)
    # num_palabras_reservadas_catExpresionesAfirmacion_distintas = len(
    #     palabras_reservadas_catExpresionesAfirmacion_distintas)
    # num_palabras_reservadas_catExpresionesNegacionDuda_distintas = \
    #     len(palabras_reservadas_catExpresionesNegacionDuda_distintas)
    # num_palabras_reservadas_catLugares_distintas = len(palabras_reservadas_catLugares_distintas)
    # num_palabras_reservadas_catDiasSemana_distintas = len(palabras_reservadas_catDiasSemana_distintas)
    # num_palabras_reservadas_catAdverbiosTemporales_distintas = len(
    #     palabras_reservadas_catAdverbiosTemporales_distintas)
    # num_palabras_reservadas_catHoras_distintas = len(palabras_reservadas_catHoras_distintas)
    # num_palabras_reservadas_catPronombresPersonales_distintas = len(
    #     palabras_reservadas_catPronombresPersonales_distintas)
    # print "=========================================================================================="
    # print "-------------"
    # print "Palabras reservadas total:", num_palabras_reservadas_total, ", de las cuales distintas:", num_palabras_reservadas_distintas
    # print "-------------"
    # print "Pronombres interrogativos:", num_palabras_reservadas_catPronombresInterrogativos, ", de los cuales distintos:", num_palabras_reservadas_catPronombresInterrogativos_distintas
    # for expresion in palabras_reservadas_catPronombresInterrogativos_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Adjetivos:", num_palabras_reservadas_catAdjetivos, ", de los cuales distintos:", num_palabras_reservadas_catAdjetivos_distintas
    # for expresion in palabras_reservadas_catAdjetivos_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Saludos o despedidas:", num_palabras_reservadas_catSaludosDespedidas, ", de los cuales distintos:", num_palabras_reservadas_catSaludosDespedidas_distintas
    # for expresion in palabras_reservadas_catSaludosDespedidas_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Frases hechas:", num_palabras_reservadas_catFrasesHechas, ", de los cuales distintos:", num_palabras_reservadas_catFrasesHechas_distintas
    # for expresion in palabras_reservadas_catFrasesHechas_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Expresiones de afirmacion:", num_palabras_reservadas_catExpresionesAfirmacion, ", de los cuales distintos:", num_palabras_reservadas_catExpresionesAfirmacion_distintas
    # for expresion in palabras_reservadas_catExpresionesAfirmacion_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Expresiones de negacion o duda:", num_palabras_reservadas_catExpresionesNegacionDuda, ", de los cuales distintos:", num_palabras_reservadas_catExpresionesNegacionDuda_distintas
    # for expresion in palabras_reservadas_catExpresionesNegacionDuda_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Lugares:", num_palabras_reservadas_catLugares, ", de los cuales distintos:", num_palabras_reservadas_catLugares_distintas
    # for expresion in palabras_reservadas_catLugares_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Dias de la semana:", num_palabras_reservadas_catDiasSemana, ", de los cuales distintos:", num_palabras_reservadas_catDiasSemana_distintas
    # for expresion in palabras_reservadas_catDiasSemana_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Adverbios temporales:", num_palabras_reservadas_catAdverbiosTemporales, ", de los cuales distintos:", num_palabras_reservadas_catAdverbiosTemporales_distintas
    # for expresion in palabras_reservadas_catAdverbiosTemporales_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Horas:", num_palabras_reservadas_catHoras, ", de los cuales distintos:", num_palabras_reservadas_catHoras_distintas
    # for expresion in palabras_reservadas_catHoras_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "Pronombres personales:", num_palabras_reservadas_catPronombresPersonales, ", de los cuales distintos:", num_palabras_reservadas_catPronombresPersonales_distintas
    # for expresion in palabras_reservadas_catPronombresPersonales_distintas:
    #     print expresion[1] + ",",
    # print "\n-------------"
    # print "=========================================================================================="