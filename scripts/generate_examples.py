#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

intent_type = sys.argv[1]

MAX_EXAMPLES = 5000
examples = 0

cities = []
with open('../resources/sorted_cities.txt', 'rb') as cities_list:
    for line in cities_list:
        cities.append(line.strip())

datetimes = ['el lunes', 'el martes', 'el miércoles', 'el jueves', 'el viernes', 'el sábado', 'el domingo',
             'hoy', 'mañana', 'pasado mañana', 'esta semana', 'en dos días', 'dentro de dos días', 'en tres días',
             'dentro de tres días', 'en cuatro días', 'dentro de cuatro días',
             'la semana que viene', 'dentro de dos semanas', 'en dos semanas', 'el mes que viene']

if intent_type == 'forecast':
    print('¿Va a hacer buen tiempo?')
    examples += 1

for d in datetimes:
    if intent_type == 'forecast':
        print('¿Qué tiempo hará [{}](forecast_start_datetime)?'.format(d))
        print('¿[{}](forecast_start_datetime) qué tiempo hará?'.format(d))
        examples += 2
    elif intent_type == 'forecast_item':
        print(
            '¿[{}](forecast_start_datetime) me llevo [chaqueta](forecast_item)?'.format(d))
        print(
            '¿Me llevo [chaqueta](forecast_item) [{}](forecast_start_datetime)?'.format(d))
        examples += 2
    elif intent_type == 'forecast_condition':
        print('¿Va a llover [{}](forecast_start_datetime)?'.format(d))
        print('¿[{}](forecast_start_datetime) va a llover?'.format(d))
        print('¿Habrá muchas nubes [{}](forecast_start_datetime)?'.format(d))
        print('¿[{}](forecast_start_datetime) habrá muchas nubes?'.format(d))
        examples += 4
    elif intent_type == 'forecast_temperature':
        print('¿Hará calor [{}](forecast_start_datetime)?'.format(d))
        print('¿[{}](forecast_start_datetime) hará calor?'.format(d))
        examples += 2

while examples < MAX_EXAMPLES - 100:
    city = random.choice(cities)
    if intent_type == 'forecast':
        print('¿Qué tiempo hay en [{}](forecast_locality)?'.format(city))
        print('¿Qué tiempo hará en [{}](forecast_locality)?'.format(city))
        examples += 2
    elif intent_type == 'forecast_item':
        print(
            '¿A [{}](forecast_locality) me llevo [chaqueta](forecast_item)?'.format(city))
        print(
            '¿Puedo ir en [pantalones cortos](forecast_item) a [{}](forecast_locality)?'.format(city))
        examples += 2
    elif intent_type == 'forecast_condition':
        print(
            '¿Va a hacer [buen tiempo](forecast_condition_name) en [{}](forecast_locality)?'.format(city))
        print(
            '¿Hará [sol](forecast_condition_name) en [{}](forecast_locality)?'.format(city))
        examples += 2
    elif intent_type == 'forecast_temperature':
        print('¿Hará frío en [{}](forecast_locality)?'.format(city))
        print('¿Hace calor en [{}](forecast_locality)?'.format(city))
        examples += 2

    for d in datetimes:
        if intent_type == 'forecast':
            print('¿Qué tiempo hará [{}](forecast_start_datetime) en [{}](forecast_locality)?'.format(
                d, city))
            print('¿Qué tiempo hará en [{}](forecast_locality) [{}](forecast_start_datetime)?'.format(
                city, d))
            print('¿[{}](forecast_start_datetime) qué tiempo hará en [{}](forecast_locality)?'.format(
                d, city))
            print('Quiero saber el tiempo que hará [{}](forecast_start_datetime) en [{}](forecast_locality)'.format(
                d, city))
            print('Quiero saber el tiempo que hará en [{}](forecast_locality) [{}](forecast_start_datetime)'.format(
                city, d))
            if d.startswith('el'):
                print('Dime el tiempo d[{}](forecast_start_datetime) en [{}](forecast_locality)'.format(
                    d, city))
            else:
                print('Dime el tiempo de [{}](forecast_start_datetime) en [{}](forecast_locality)'.format(
                    d, city))
            examples += 6
        elif intent_type == 'forecast_item':
            print(
                '¿Neceistaré [gafas de sol](forecast_item) en [{}](forecast_locality) [{}](forecast_start_datetime)?'.format(city, d))
            print(
                '¿Neceistaré [gafas de sol](forecast_item) [{}](forecast_start_datetime) en [{}](forecast_locality)?'.format(d, city))
            print(
                '¿[{}](forecast_start_datetime) neceistaré [gafas de sol](forecast_item) en [{}](forecast_locality)?'.format(d, city))
            print(
                '¿Voy a necesitar [paraguas](forecast_item) en [{}](forecast_locality) [{}](forecast_start_datetime)?'.format(city, d))
            print(
                '¿Voy a necesitar [paraguas](forecast_item) [{}](forecast_start_datetime) en [{}](forecast_locality)?'.format(d, city))
            print(
                '¿[{}](forecast_start_datetime) voy a necesitar [paraguas](forecast_item) en [{}](forecast_locality)?'.format(d, city))
            examples += 6
        elif intent_type == 'forecast_condition':
            print('¿[Granizará](forecast_condition_name) [{}](forecast_start_datetime) en [{}](forecast_locality)?'.format(
                d, city))
            print('¿[{}](forecast_start_datetime) [granizará](forecast_condition_name) en [{}](forecast_locality)?'.format(
                d, city))
            print('¿[Granizará](forecast_condition_name) en [{}](forecast_locality) [{}](forecast_start_datetime)?'.format(
                city, d))
            print('¿Hará [buen tiempo](forecast_condition_name) en [{}](forecast_locality) [{}](forecast_start_datetime)?'.format(
                city, d))
            print('¿Hará [buen tiempo](forecast_condition_name) [{}](forecast_start_datetime) en [{}](forecast_locality)?'.format(
                d, city))
            print('¿[{}](forecast_start_datetime) hará [buen tiempo](forecast_condition_name) en [{}](forecast_locality)?'.format(
                d, city))
            examples += 6
        elif intent_type == 'forecast_temperature':
            print('¿Hará frío [{}](forecast_start_datetime)?'.format(d))
            print('¿[{}](forecast_start_datetime) hará frío?'.format(d))
            print('¿Hace calor [{}](forecast_start_datetime)?'.format(d))
            print('¿[{}](forecast_start_datetime) hace calor?'.format(d))
            examples += 4
