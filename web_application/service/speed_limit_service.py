
"""

Maybe this code will be useful someday...
But nowadays, it is.

"""

def get_street(coordinate):
    # get coordinate on google maps.
    # persist it on elastic-search.
    return "oi"


def enrich_coordinates_with_speed_limit(coordinates, begin_index, end_index, begin_street):
    for i in range(begin_index, end_index):
        coordinates[i]['speed_limit'] = begin_street


def recursive_enricher_speed_limit(coordinates, begin_index, end_index):
    """
    CAUTION: this method changes the coordinates index! Be careful when using it.
    If you feell motivated, you can do it in a functional and parallelizable way.
    """
    begin_street = get_street(coordinates[begin_index])
    end_street = get_street(coordinates[end_index])

    if begin_street == end_street:
        enrich_coordinates_with_speed_limit(coordinates, begin_index, end_index, begin_street)
    else:
        recursive_enricher_speed_limit(coordinates, begin_index, end_index / 2)
        recursive_enricher_speed_limit(coordinates, end_index / 2, end_index)
