import numpy as np
import requests
import xmltodict, json


#
# http://wiki.openstreetmap.org/wiki/Downloading_data#Construct_a_URL_for_the_HTTP_API
#

# left, bottom, right, top (min long, min lat, max long, max lat)
URL = "http://api.openstreetmap.org/api/0.6/map?bbox={},{},{},{}"

def naosei(coordinates):
    latitudes = list(map(lambda x: x['lat'], coordinates))
    longitudes = list(map(lambda x: x['lng'], coordinates))

    # essa ideia de separar em quartis pareceu boa.
    # devo continuar com ela.
    left = np.min(longitudes)
    right = np.percentile(longitudes, .25)
    top = np.percentile(latitudes, .25)
    bottom = np.min(latitudes)

    req_url = URL.format(left, bottom, right, top)
    response = requests.get(req_url)
    payload = response.content.decode('utf-8')

    my_dict = xmltodict.parse(payload)

    print("ae")
    print("oi")

