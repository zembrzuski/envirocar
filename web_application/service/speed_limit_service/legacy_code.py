
def find_traces_for_way(trace, ways):
    enriched_traces = list()

    for way in ways:

        enriched_trace = list(map(lambda x: enrich_way_with_similatiry_to_trace(x, trace), way))
        enriched_traces.append(enriched_trace)

        #filtered_way = list(filter(lambda x: x.get('name', '') == trace['long_name'] or x.get('name', '') == trace['short_name'], way))
        #filtered_ways.append(filtered_way)

    return None

def enrich_way_with_similatiry_to_trace(way, trace):
    new_way = copy.deepcopy(way)

    new_way['long_name_similarity'] = similar(trace.get('long_name', ''), way.get('name', ''))
    new_way['short_name_similarity'] = similar(trace.get('short_name', ''), way.get('name', ''))

    return new_way

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
