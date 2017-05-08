import numpy as np
import requests
import web_application.service.openstreetmap_parser as parser

#
# http://wiki.openstreetmap.org/wiki/Downloading_data#Construct_a_URL_for_the_HTTP_API
#

# left, bottom, right, top (min long, min lat, max long, max lat)
URL = "http://api.openstreetmap.org/api/0.6/map?bbox={},{},{},{}"

def do_many_things(coordinates):
    latitudes = list(map(lambda x: x['lat'], coordinates))
    longitudes = list(map(lambda x: x['lng'], coordinates))

    # TODO separar em 4 lugares esse cara.
    left = np.min(longitudes)
    right = np.mean(longitudes)
    top = np.mean(latitudes)
    bottom = np.min(latitudes)

    req_url = URL.format(left, bottom, right, top)
    response = requests.get(req_url)
    payload = response.content.decode('utf-8')

    #my_dict = xmltodict.parse(payload)
    ways_information = parser.do_the_parsing(payload)

    for xoxo in ways_information:
        if 'maxspeed' in xoxo:
            print(xoxo['maxspeed'])



    print("ae")
    print("oi")

