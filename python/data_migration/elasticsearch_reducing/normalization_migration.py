import requests
import python.data_migration.elasticsearch_reducing.normalizing_data as normalization


HOST = '192.168.0.13'



my_query = {
    "bool": {
      "must": [
        {"match_all": {}}
      ],
      "filter": [
        { "range": { "features.linha_reta_distance": { "gte": 1 } } },
        { "range": { "features.rpm.mean": { "gte": 0 } } },
        { "range": { "features.co2.mean": { "gte": 0.1 } } },
        { "term":  { "features.speed.unit.keyword": "km/h" } }
      ]
    }
}

my_aggs = {
    "co2_stats": { "stats": { "field": "features.co2.mean" } },
    "duration_stats": { "stats": { "field": "features.duration_seconds" } },
    "speed_stats": { "stats": { "field": "features.speed.mean" } },
    "linha_reta_distance_stats": { "stats": { "field": "features.linha_reta_distance" } },
    "rpm_stats": { "stats": { "field": "features.rpm.mean" } },
    "consumption_stats": { "stats": { "field": "features.consumption.mean" } },
    "total_distance_stats": { "stats": { "field": "features.total_distance" } }
}



def start_scrolling():
    url = 'http://{host}:9200/envirocar_reduced_3/group/_search?scroll=20m'.format(host=HOST)

    query = {
        "size": 10,
        "query": my_query,
        "aggs": my_aggs,
        "sort": [
            "_doc"
        ]
    }

    response = requests.post(url, json=query).json()

    return response['_scroll_id']




def query_a_page(scroll_id):
    url = 'http://{host}:9200/_search/scroll'.format(host=HOST)

    query = {
        "scroll": "20m",
        "scroll_id": scroll_id
    }

    response = requests.post(url, json=query).json()

    for resp in response['hits']['hits']:
        to_update = normalization.compute_normalized_fields(resp)
        url = 'http://{host}:9200/envirocar_reduced_3/group/{id}/_update'.format(host=HOST, id=resp['_id'])
        status_code = requests.post(url, json=to_update).status_code
        print(status_code)

    print("foooi.")



if __name__ == '__main__':

    scroll_id = start_scrolling()

    while True:
        query_a_page(scroll_id)

