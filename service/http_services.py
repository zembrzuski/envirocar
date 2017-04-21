import requests
import json


def request_json(url):
    """ Request an url, parse its json response and returns the given dictionary."""
    return json.loads(requests.get(url).content.decode('utf-8'))
