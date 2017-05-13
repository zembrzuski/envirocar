
def find_trace_for_coordinate(coord_idx, enriched_traces):
    # procuro trace cujo index eh maior ao coord_idx
    # retorno o anterior
    # se nao acho, retorno o ultimo trace possivel
    for i in range(0, len(enriched_traces)):
        current_trace = enriched_traces[i]
        if current_trace['index'] > coord_idx:
            return enriched_traces[i-1]

    return enriched_traces[len(enriched_traces)-1]



def enrich(enriched_traces, coordinates):
    """ Be careful. this method changes coordinates var. i made it because python is too slow."""
    for idx in range(0, len(coordinates)):
        trace = find_trace_for_coordinate(idx, enriched_traces)
        coordinates[idx]['trace'] = trace

    return coordinates