import service.http_services as http_services
import json

TRACKS_BASE_URL = 'https://envirocar.org/api/stable/tracks'


def retrieve_track_ids_from_first_page():
    """
    Request the first track pages and return the tracks ids. With this ids, it is possible
    to download all of them to retrieve its information.
    """
    response = http_services.request_json(TRACKS_BASE_URL)
    tracks_ids = list(map(lambda x: x['id'], response['tracks']))
    return tracks_ids


def write_to_file(track_id):
    """
    Download a track and persist it to the filesystem.
    """
    track_response = http_services.request_json(TRACKS_BASE_URL + "/{}".format(track_id))

    with open("data_input/{}.json".format(track_id), "w") as text_file:
        text_file.write(json.dumps(track_response))

    print('done: {}'.format(track_id))
    return track_response
