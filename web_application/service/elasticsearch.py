import json

import numpy as np
import requests
from dateutil.parser import parse

import web_application.service.address_service.all_streets_route_interpolator as route_interpolator
import web_application.service.distance_functions as distance_functions


def create_dict_to_phenomenon(phenomenons, attribute):
    try:
        values = list(map(lambda x: x[attribute]['value'], phenomenons))

        the_dict = {
            'max': np.max(values),
            'med': np.mean(values),
            'min': np.min(values),
            'unit': phenomenons[0][attribute]['unit'],
        }

        print(the_dict)

        return the_dict
    except:
        return {
            'max': 0,
            'med': 0,
            'min': 0,
            'unit': "NA",
        }


def retrieve_by_id(track):
    resp = requests.get('http://localhost:9200/envirocar/group/{}'.format(track))
    loaded = json.loads(resp.content.decode('utf-8'))

    features = loaded['_source']['features']

    coords = list(map(lambda x: x['geometry']['coordinates'], features))
    coordinates = list(map(lambda x: {'lng': x[0], 'lat': x[1]}, coords))
    phenomenons = list(map(lambda x: x['properties']['phenomenons'], features))
    timestamps = list(map(lambda x: parse(x['properties']['time']), features))

    #openstreetmap_servicce.do_many_things(coordinates)
    route_interpolator.get_route(coordinates)

    lat_center = np.mean(list(map(lambda x: x[1], coords)))
    lng_center = np.mean(list(map(lambda x: x[0], coords)))

    inicio = timestamps[0]
    fim = timestamps[-1]
    duration = timestamps[-1] - timestamps[0]

    return json.dumps({
        'center': {
            'lat': lat_center,
            'lng': lng_center
        },
        'coordinates': coordinates,
        'phenomenons': phenomenons,
        'vel': create_dict_to_phenomenon(phenomenons, 'Speed'),
        'co2': create_dict_to_phenomenon(phenomenons, 'CO2'),
        'rpm': create_dict_to_phenomenon(phenomenons, 'Rpm'),
        'engine-load': create_dict_to_phenomenon(phenomenons, 'Engine Load'),
        'total-distance': distance_functions.compute_distance(coordinates),
        'linha-reta-distance': distance_functions.compute_distance([coordinates[0], coordinates[-1]]),
        'tempo-inicio': str(inicio),
        'tempo-fim': str(fim),
        'duracao': str(duration),
        'vm': distance_functions.compute_distance(coordinates)/(duration.seconds/60/60),
    })
