import web_application.service.address_service.address_retrieval_google_maps as gmaps


"""
This is a terrible implementation of an algorithm to retrieve all the
streets that a car passed by in a given track.
"""

def flatten(x, flatted_list):
    if isinstance(x, list):
        for l in x:
            flatted_list.append(flatten(l, flatted_list))
        return flatted_list
    else:
        return x


def get_route_recursive(coordinates, begin_index, end_index, begin_addr, end_addr):
    print("ae " + str(begin_index) + " " + str(end_index))

    if begin_addr:
        add1 = begin_addr
    else:
        add1 = gmaps.retrieve_address_by_coordinate(coordinates[begin_index]['lat'], coordinates[begin_index]['lng'])

    if end_addr:
        add2 = end_addr
    else:
        add2 = gmaps.retrieve_address_by_coordinate(coordinates[end_index]['lat'], coordinates[end_index]['lng'])

    if add1[0].get('long_name') == add2[0].get('long_name') or begin_index+1==end_index:
        return [add1]
    else:
        middle = int((begin_index + end_index) / 2)
        r1 = get_route_recursive(coordinates, begin_index, middle, add1, None)
        r2 = get_route_recursive(coordinates, middle, end_index, None, add2)
        r1.append(r2)
        return r1


def get_route(coordinates):
    """
    This is a terrible implementation of an algorithm to retrieve all the
    streets that a car passed by in a given track.
    """
    r1 = get_route_recursive(coordinates, 0, int(len(coordinates) / 2), None, None)
    r2 = get_route_recursive(coordinates, int((len(coordinates) - 1) / 2), int(len(coordinates) - 1), None, None)

    r1.append(r2)

    trace = list(map(lambda x: x['long_name'], list(filter(lambda x: isinstance(x, dict), flatten(r1, [])))))

    print("\n".join(trace))

    return trace
