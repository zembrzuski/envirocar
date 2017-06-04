#import python.service.http_services as http_services
import http_services as http_services
import json
import requests

ELASTICSEARCH_URL = 'http://192.168.0.13:9200'


def retrieve_track_ids_given_a_page(page):
    """
    Request the first track pages and return the tracks ids. With this ids, it is possible
    to download all of them to retrieve its information.
    """
    response = http_services.request_json('https://envirocar.org/api/stable/tracks?page={}'.format(page))
    tracks_ids = list(map(lambda x: x['id'], response['tracks']))
    return tracks_ids


def retrieve_a_track_given_an_id(track_id):
    """
    Download a track
    """
    print('retrieving {}'.format(track_id))
    track_response = http_services.request_json('https://envirocar.org/api/stable/tracks' + "/{}".format(track_id))
    print('retrieved {}'.format(track_id))
    return track_response


def enriched_track_with_linestring(track):
    track['location'] = dict()
    track['location']['type'] = 'linestring'
    track['location']['coordinates'] = list(map(lambda x: x['geometry']['coordinates'], track['features']))
    return track


def post_track_to_elasticsearch(elasticsearch_url, track):
    id_ = track['properties']['id']
    group_ = '{}/envirocar/group/{}'.format(elasticsearch_url, id_)
    resp = requests.post(group_, json.dumps(track))
    return resp


def already_imported(the_id):
    response = requests.get(ELASTICSEARCH_URL + "/envirocar/group/" + the_id)
    return response.json()['found']


def process_tracks(the_idds):
    for the_id in the_idds:
        print('start {}'.format(the_id))
        if already_imported(the_id):
            print('skipped {}'.format(the_id))
            continue
        the_track = retrieve_a_track_given_an_id(the_id)
        print('got {}'.format(the_id))
        enriched_track = enriched_track_with_linestring(the_track)
        resp = post_track_to_elasticsearch(ELASTICSEARCH_URL, enriched_track)
        if resp.status_code != 200 and resp.status_code != 201:
            print("error")
        else:
            print('gone {}'.format(the_id))


if __name__ == '__main__':
    for i in range(0, 148):
        print(i)
        the_ids = retrieve_track_ids_given_a_page(i)
        print('retrieved page {}'.format(i))
        process_tracks(the_ids)
