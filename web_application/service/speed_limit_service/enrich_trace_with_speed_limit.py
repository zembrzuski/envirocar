import numpy as np
import copy

def find_traces_for_way(trace, ways):
    filtered_ways = list()

    for way in ways:
        filtered_way = list(filter(lambda x: x.get('name', '') == trace['long_name']
                        or x.get('name', '') == trace['short_name'], way))

        filtered_ways.append(filtered_way)

    return filtered_ways


def discover_maxspeed_for_way(filtered_ways):
    speedss = list()

    for w in filtered_ways:
        speeds = list(filter(lambda y: y != -1, (map(lambda x: float(x.get('maxspeed', -1)), w))))
        for x in speeds:
            speedss.append(x)

    mean = np.mean(speedss)

    if len(speedss) == 0:
        return 0

    if mean != speedss[0]:
        print("warning. the speed limit I am returning may be wrong.")

    return mean


def execute(all_traces, ways):
    enriched_traces = list()

    for trace in all_traces:
        new_trace = copy.deepcopy(trace)
        filtered_ways = find_traces_for_way(trace, ways)
        new_trace['maxspeed'] = discover_maxspeed_for_way(filtered_ways)
        enriched_traces.append(new_trace)

    return enriched_traces