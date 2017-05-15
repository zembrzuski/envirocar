import redis
import requests
import json

API_KEY = "AIzaSyDehTfquJd2bxKy3kHRbZ-Ml23aP4YZfd8"
URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}"


def retrieve_address_by_coordinate(lat, lng):
    """
    Given a coordinate, retrieves the street information supposed to be.
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_key = str(lat) + "___" + str(lng)
    cached_url = r.get(redis_key)

    the_json = None

    if cached_url:
        the_json = json.loads(cached_url.decode('utf-8'))
    else:
        response = requests.get(URL.format(lat, lng, API_KEY))
        the_json = json.loads(response.content.decode('utf-8'))
        r.set(redis_key, json.dumps(the_json))

    addresses_components = list(map(lambda x: x['address_components'], the_json['results']))

    routes = list()
    for addresss in addresses_components:
        for type in addresss:
            if any("route" in s for s in type['types']):
                routes.append(type)

    return routes




#routes = retrieve_address_by_coordinate(51.522755172965105, 6.990312188176352)
#print(routes)