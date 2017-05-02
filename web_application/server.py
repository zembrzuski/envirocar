from flask import Flask
from flask import send_file
import requests
import json
import numpy as np

app = Flask(__name__)


@app.route('/map/<track>')
def send_js(track):
    return send_file('teste.html')


@app.route('/find_track/<track>')
def find_track(track):
    resp = requests.get('http://localhost:9200/envirocar/group/{}'.format(track))
    loaded = json.loads(resp.content.decode('utf-8'))

    features = loaded['_source']['features']

    coords = list(map(lambda x: x['geometry']['coordinates'], features))
    coordinates = list(map(lambda x: {'lng': x[0], 'lat': x[1]}, coords))

    lat_center = np.mean(list(map(lambda x: x[1], coords)))
    lng_center = np.mean(list(map(lambda x: x[0], coords)))

    return json.dumps({
        'center': {
            'lat': lat_center,
            'lng': lng_center
        },
        'coordinates': coordinates
    })


if __name__ == "__main__":
    app.run()
