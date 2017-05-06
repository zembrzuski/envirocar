from geopy.distance import vincenty


def compute_distance(coordinates):
    total = 0
    for i in range(0, len(coordinates)-1):
        a = coordinates[i]
        b = coordinates[i + 1]
        aa = (a['lat'], a['lng'])
        bb = (b['lat'], b['lng'])
        total += vincenty(aa, bb).kilometers
    return total
