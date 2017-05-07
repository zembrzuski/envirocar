import requests
import json

###
### load speed limits using google roads api.
### https://developers.google.com/maps/documentation/roads/speed-limits
###

#
ROADS_API_URL = "https://roads.googleapis.com/v1/speedLimits?path={}&key=AIzaSyAq1-E7zQOTLiZ5pjLMMEETkYlns8T2VS0"


def get_speed_limit_for_path(coordinates):
    pairs = list(map(lambda x: str(x['lat']) + "," + str(x['lng']), coordinates))
    pipe = "|".join(pairs)
    response = requests.get(ROADS_API_URL.format(pipe))
    parsed = json.loads(response.content.decode("utf-8"))
    return parsed
