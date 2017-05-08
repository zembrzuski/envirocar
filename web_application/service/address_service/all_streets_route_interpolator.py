import web_application.service.address_service.address_retrieval_google_maps as gmaps


def get_route_rec(coordinates, begin, end):
    """
    Given many points, try to discover all streets that the user passed by
    """

    print("ae " + str(begin) + " " + str(end))

    add1 = gmaps.retrieve_address_by_coordinate(coordinates[begin]['lat'], coordinates[begin]['lng'])
    add2 = gmaps.retrieve_address_by_coordinate(coordinates[end]['lat'], coordinates[end]['lng'])

    if add1[0].get('long_name') == add2[0].get('long_name') or begin+1==end:
        return [add1]
    else:
        middle = int((begin+end)/2)
        r1 = get_route_rec(coordinates, begin, middle)
        r2 = get_route_rec(coordinates, middle, end)
        return r1.append(r2)


def get_route(coordinates):
    r1 = get_route_rec(coordinates, 0, int(len(coordinates)/2))
    r2 = get_route_rec(coordinates, int((len(coordinates)-1) / 2), int(len(coordinates)-1))

    return r1.append(r2)
