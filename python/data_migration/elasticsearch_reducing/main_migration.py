import requests
from dateutil.parser import parse
import math
from geopy.distance import vincenty

HOST = '192.168.0.13'


def compute_distance(coordinates):
    total = 0
    for i in range(0, len(coordinates) - 1):
        a = coordinates[i]
        b = coordinates[i + 1]
        aa = (a[1], a[0])
        bb = (b[1], b[0])
        total += vincenty(aa, bb).kilometers
    return total


def compute_avg(attribute, features):
    filtered = list(filter(lambda feature: attribute in feature['properties']['phenomenons'], features))
    all_values = list(map(lambda feature: feature['properties']['phenomenons'][attribute]['value'], filtered))
    mean = float(sum(all_values)) / len(all_values) if len(all_values) > 0 else 0
    sd = math.sqrt(float(sum(list(map(lambda x: (x - mean) ** 2, all_values)))) / len(all_values)) if len(
        all_values) > 0 else 0

    return {
        'mean': mean,
        'sd': sd,
        'max': max(all_values) if len(all_values) > 0 else 0,
        'min': min(all_values) if len(all_values) > 0 else 0,
        'unit': filtered[0]['properties']['phenomenons'][attribute]['unit'] if len(all_values) > 0 else 'N/A'
    }


def reduce_a_document_and_persist_it(document):
    document_id = document['_id']

    found = requests.get('http://192.168.0.13:9200/envirocar_reduced_2/group/{doc_id}'.format(doc_id=document_id)).json()['found']

    if found:
        print("skipping: {}".format(document_id))
        return 0




    print("trying to import: {}".format(document_id))

    resp = document

    init_timestamp = resp['_source']['features'][0]['properties']['time']
    finish_timestamp = resp['_source']['features'][-1]['properties']['time']
    coordinates = resp['_source']['location']['coordinates']

    reduced_document = {
        'path': {
            'coordinates': coordinates,
            'type': 'linestring'
        },
        'sensor': resp['_source']['properties']['sensor'],
        'features': {
            'co2': compute_avg('CO2', resp['_source']['features']),
            'consumption': compute_avg('Consumption', resp['_source']['features']),
            'rpm': compute_avg('Rpm', resp['_source']['features']),
            'speed': compute_avg('Speed', resp['_source']['features']),
            'init_timestamp': init_timestamp,
            'finish_timestamp': finish_timestamp,
            'duration_seconds': (parse(finish_timestamp) - parse(init_timestamp)).seconds,
            'total_distance': compute_distance(coordinates),
            'linha_reta_distance': compute_distance([coordinates[0], coordinates[-1]]),
            'init_point': {
                'type': 'point',
                'coordinates': coordinates[0]
            },
            'finish_point': {
                'type': 'point',
                'coordinates': coordinates[-1]
            }
        }
    }

    status_code = requests.post(
        'http://192.168.0.13:9200/envirocar_reduced_2/group/{doc_id}'.format(doc_id=document_id),
        json=reduced_document
    ).status_code

    if status_code == 200 or status_code == 201:
        print("finished to import: {}".format(document_id))
        return 0

    print("failed to import: {}".format(document_id))
    return -1


def query_a_page(scroll_id):
    url = 'http://{host}:9200/_search/scroll'.format(host=HOST)

    query = {
        "scroll": "20m",
        "scroll_id": scroll_id
    }

    response = requests.post(url, json=query).json()

    hits_ = response['hits']['hits']

    for resp in hits_:
        reduce_a_document_and_persist_it(resp)

    print("foooi.")


def start_scrolling():
    url = 'http://{host}:9200/envirocar/group/_search?scroll=20m'.format(host=HOST)

    query = {
        "size": 30,
        "sort": [
            "_doc"
        ]
    }

    response = requests.post(url, json=query).json()

    return response['_scroll_id']


if __name__ == '__main__':

    scroll_id = start_scrolling()

    while True:
        query_a_page(scroll_id)
