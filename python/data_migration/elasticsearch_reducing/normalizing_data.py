import requests

"""
O que esse arquivo vai fazer?

- vou normalizar os dados para poder fazer uma visualização em radar.
- sao filtrados cara que percorrem menos de 1km, pq eles são irrelevantes.
- sao filtrados caras cujo co2 eh menor do que 0.1. Com isso, saem todos
  os dados cujo co2 eh zero. Com isso, eliminam-se dados faltantes.

- alem disso, os dados vao ser normalizados, devido a uma limitacao da
  biblioteca que plota radar do elasticserach, pois todos os eixos
  possuem a mesma escala.
"""


stats_for_normalization = {
    "linha_reta_distance_stats": {
        "count": 6777,
        "min": 1,
        "max": 491,
        "avg": 13.882839014313118,
        "sum": 94084
    },
    "duration_stats": {
        "count": 6777,
        "min": 35,
        "max": 74407,
        "avg": 1377.0081156854064,
        "sum": 9331984
    },
    "rpm_stats": {
        "count": 6777,
        "min": 0,
        "max": 4408.37451171875,
        "avg": 1730.7432962738167,
        "sum": 11729247.318847656
    },
    "consumption_stats": {
        "count": 6777,
        "min": 0.0005000392557121813,
        "max": 29.41737937927246,
        "avg": 3.467426923752667,
        "sum": 23498.752262271824
    },
    "speed_stats": {
        "count": 6777,
        "min": 5.605193138122559,
        "max": 139.78988647460938,
        "avg": 45.76777970919272,
        "sum": 310168.24308919907
    },
    "co2_stats": {
        "count": 6777,
        "min": 1.2591140270233154,
        "max": 77.9560546875,
        "avg": 8.193475966962263,
        "sum": 55527.186628103256
    },
    "total_distance_stats": {
        "count": 6777,
        "min": 1,
        "max": 621,
        "avg": 19.77984358860853,
        "sum": 134048
    }
}



# feature_to_normalize == co2
# feature_stats_fireld == co2_stats
def do_normalization(rsp, feature_to_normalize, feature_stats_field):
    return (rsp['_source']['features'][feature_to_normalize]['mean'] - stats_for_normalization[feature_stats_field]['min']) / (stats_for_normalization[feature_stats_field]['max'] - stats_for_normalization[feature_stats_field]['min'])


def do_normalization_special_case(rsp, feature_to_normalize, feature_stats_field):
    return (rsp['_source']['features'][feature_to_normalize] - stats_for_normalization[feature_stats_field]['min']) / (stats_for_normalization[feature_stats_field]['max'] - stats_for_normalization[feature_stats_field]['min'])


def simple_request():
    rsp = requests.get('http://192.168.0.13:9200/envirocar_reduced_3/group/59084a4e268d1b08a47bb169').json()

    co2_normalized = do_normalization(rsp, 'co2', 'co2_stats')
    rpm_normalized = do_normalization(rsp, 'rpm', 'rpm_stats')
    consumption_normalized = do_normalization(rsp, 'consumption', 'consumption_stats')
    speed_normalized = do_normalization(rsp, 'speed', 'speed_stats')

    linha_reta_distancce_normalized = do_normalization_special_case(rsp, 'linha_reta_distance', 'linha_reta_distance_stats')
    duration_normalized = do_normalization_special_case(rsp, 'duration_seconds', 'duration_stats')
    total_distance_normalized = do_normalization_special_case(rsp, 'total_distance', 'total_distance_stats')

    new_fields_to_post = {'features': {
        'co2': {},
        'rpm': {},
        'consumption': {},
        'speed': {}
    }}

    new_fields_to_post['features']['co2']['normalized'] = co2_normalized
    new_fields_to_post['features']['rpm']['normalized'] = rpm_normalized
    new_fields_to_post['features']['consumption']['normalized'] = consumption_normalized
    new_fields_to_post['features']['speed']['normalized'] = speed_normalized
    new_fields_to_post['features']['linha_reta_distance_normalized'] = linha_reta_distancce_normalized
    new_fields_to_post['features']['total_distance_normalized'] = total_distance_normalized
    new_fields_to_post['features']['duration_seconds_normalized_normalized'] = duration_normalized

    # do the update now.

    to_update = {
        'doc': new_fields_to_post
    }

    post_resp = requests.post('http://192.168.0.13:9200/envirocar_reduced_3/group/59084a4e268d1b08a47bb169/_update', json=to_update)
    print("oi")


if __name__ == '__main__':
    simple_request()
    print("oi")
