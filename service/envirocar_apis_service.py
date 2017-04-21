import service.http_services as http_services

TRACKS_BASE_URL = 'https://envirocar.org/api/stable/tracks'


def retrieve_track_ids_from_first_page():
    """
    Request the first track pages and return the tracks ids. With this ids, it is possible
    to download all of them to retrieve its information.
    """
    response = http_services.request_json(TRACKS_BASE_URL)
    tracks_ids = list(map(lambda x: x['id'], response['tracks']))
    return tracks_ids
