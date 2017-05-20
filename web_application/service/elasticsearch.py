import redis
import json
import copy
import numpy as np
import requests
from dateutil.parser import parse

import web_application.service.address_service.all_streets_route_interpolator as route_interpolator
import web_application.service.distance_functions as distance_functions
import web_application.service.speed_limit_service.openstreetmap_region_retrieval as region_retrieval
import web_application.service.speed_limit_service.enrich_trace_with_speed_limit as enrich_trace_with_speed_limit
import web_application.service.speed_limit_service.enrich_coords_with_speed_limit as enrich_coords_with_speed_limit

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
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    cached_payload = r.get(track)

    #if cached_payload:
    #    print('returning cached info')
    #    return cached_payload

    resp = requests.get('http://localhost:9200/envirocar/group/{}'.format(track))
    loaded = json.loads(resp.content.decode('utf-8'))

    features = loaded['_source']['features']

    coords = list(map(lambda x: x['geometry']['coordinates'], features))
    coordinates = list(map(lambda x: {'lng': x[0], 'lat': x[1]}, coords))
    phenomenons = list(map(lambda x: x['properties']['phenomenons'], features))
    timestamps = list(map(lambda x: parse(x['properties']['time']), features))

    ways = region_retrieval.retrieve_region_ways(coordinates)
    trace = route_interpolator.get_route(coordinates)
    enriched_trace = enrich_trace_with_speed_limit.execute(trace, ways)

    print("----")
    print('\n'.join(list(map(lambda x: x['long_name'] + " - " + str(x['maxspeed']), enriched_trace))))
    print("----")

    coordinates = enrich_coords_with_speed_limit.enrich(enriched_trace, coordinates)

    lat_center = np.mean(list(map(lambda x: x[1], coords)))
    lng_center = np.mean(list(map(lambda x: x[0], coords)))

    inicio = timestamps[0]
    fim = timestamps[-1]
    duration = timestamps[-1] - timestamps[0]

    coords_to_export = list()
    for i in range(0, len(coordinates)):
        x = copy.deepcopy(coordinates[i])
        x['phenomenons'] = phenomenons[i]
        x['timestamp'] = str(timestamps[i])
        x['index'] = i
        coords_to_export.append(x)

    to_return = json.dumps({
        'center': {
            'lat': lat_center,
            'lng': lng_center
        },
        'coordinates': coords_to_export,
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

    r.set(track, to_return)
    return to_return
