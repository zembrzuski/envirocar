import requests
from dateutil.parser import parse
import math

def compute_avg(attribute, features):
    filtered = list(filter(lambda feature: attribute in feature['properties']['phenomenons'], features))
    all_values = list(map(lambda feature: feature['properties']['phenomenons'][attribute]['value'], filtered))
    mean = float(sum(all_values)) / len(all_values)
    sd = math.sqrt(float(sum(list(map(lambda x: (x-mean)**2, all_values))))/len(all_values))

    return {
        'mean': mean,
        'sd': sd,
        'unit': filtered[0]['properties']['phenomenons'][attribute]['unit']
    }


def reduce_a_document(doc_id):
    resp = requests.get('http://192.168.0.13:9200/envirocar/group/{doc_id}'.format(doc_id=doc_id)).json()

    document_id = resp['_id']

    init_timestamp = resp['_source']['features'][0]['properties']['time']
    finish_timestamp = resp['_source']['features'][-1]['properties']['time']

    reduced_document = {
        'path': {
            'coordinates': resp['_source']['location']['coordinates'],
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
            'duration_seconds': (parse(finish_timestamp) - parse(init_timestamp)).seconds
        }
    }

    status_code = requests.post(
        'http://192.168.0.13:9200/envirocar_reduced/group/{doc_id}'.format(doc_id=doc_id),
        json=reduced_document
    ).status_code

    if status_code == 200 or status_code == 201:
        return 0

    return -1



if __name__ == '__main__':
    print(reduce_a_document('59316569268d1b08a4abee8e'))
