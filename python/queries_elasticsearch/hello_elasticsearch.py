import requests
import json

the_query = """
{
  "query": {
    "bool": {
      "must":  {"match_all": {}},
      "filter": {
        "geo_bounding_box": {
          "features.five_points": {
            "top_left": {
              "lat": top_left_lat,
              "lon": top_left_long
            },
            "bottom_right": {
              "lat": bottom_rigth_lat,
              "lon": bottom_right_long
            }
          }
        }
      }
    }
  },
  "_source": [
    "sensor.properties.manufacturer",
    "sensor.properties.model"
  ],
  "size": 50
}
"""

def do_the_query(top_left_lat, top_left_long, bottom_rigth_lat, bottom_rigth_long):
    query = the_query\
        .replace("top_left_lat", str(top_left_lat))\
        .replace("top_left_long", str(top_left_long))\
        .replace("bottom_rigth_lat", str(bottom_rigth_lat))\
        .replace("bottom_right_long", str(bottom_rigth_long))

    loaded = json.loads(query)

    resp = requests.post('http://192.168.0.13:9200/envirocar_reduced_3/group/_search', json=loaded)

    lambda_roots = lambda x: x['_id'] + "\t" + x['_source']['sensor']['properties']['model'] + "\t" + x['_source']['sensor']['properties']['manufacturer']

    the_list = list(map(lambda_roots, resp.json()['hits']['hits']))
    to_print = '\n'.join(the_list)
    print(to_print)

    return "Ok"




# brasil
#do_the_query(5.24, -69, -31, 30)

# australia
#do_the_query(6.4, 102, -47, 165)

# india
#do_the_query(43, 46, 6.4, 102)


# estados unidos
do_the_query(49.3, -125, 24.6, -57)

print("deu")