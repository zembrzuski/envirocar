
def get_speed_limit_for_brazil(way):
    print(way['highway'])
    return 0

def try_to_know_limit_with_other_data(possible_ways):
    for x in possible_ways:
        return get_speed_limit_for_brazil(x)
    return 0
