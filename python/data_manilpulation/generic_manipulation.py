from dateutil.parser import parse as date_parser


def compute_duration_of_a_track(a_track):
    features_from_a_track = a_track['features']
    time_from_a_track = list(map(lambda feature: feature['properties']['time'], features_from_a_track))

    a = date_parser(time_from_a_track[0])
    b = date_parser(time_from_a_track[-1])

    total_minutes = float((b-a).seconds)/60

    return total_minutes


def extract_speed(a_track):
    features_from_a_track = a_track['features']

    try:
        speeds = list(map(lambda feature: feature['properties']['phenomenons']['Speed'], features_from_a_track))
    except:
        print("ae")
        return list()

    if speeds[0]['unit'] != 'km/h':
        print(speeds[0]['unit'])
        raise Exception

    return list(map(lambda x: x['value'], speeds))


def extract_position(a_track):
    features_from_a_track = a_track['features']

    coordinates = list(map(lambda feature: feature['geometry']['coordinates'], features_from_a_track))

    return coordinates