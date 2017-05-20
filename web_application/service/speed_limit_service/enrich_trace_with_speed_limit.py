import numpy as np
import copy
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()



def find_ways_for_trace(trace, ways):
    possible_ways = list()

    for way_item in ways:
        for way in way_item:
            short_name_similarity = similar(trace['short_name'], way.get('name', ''))
            long_name_similarity = similar(trace['long_name'], way.get('name', ''))

            if short_name_similarity > .8 or long_name_similarity > .8:
                possible_ways.append(way)

    return possible_ways


def try_to_know_limit_with_other_data(possible_ways):
    for x in possible_ways:
        print(x)
    return 0


def discover_maxspeed_for_way(possible_ways):
    maxspeeds = list(map(lambda x: float(x['maxspeed']), (filter(lambda x: 'maxspeed' in x, possible_ways))))

    if len(maxspeeds) == 0:
        return try_to_know_limit_with_other_data(possible_ways)

    mean = np.mean(maxspeeds)
    if (mean != maxspeeds[0]):
        print("maxspeed is probably wrong")

    return mean


def execute(all_traces, ways):
    enriched_traces = list()

    for trace in all_traces:
        new_trace = copy.deepcopy(trace)

        possible_ways = find_ways_for_trace(trace, ways)
        new_trace['maxspeed'] = discover_maxspeed_for_way(possible_ways)

        enriched_traces.append(new_trace)

    return enriched_traces