def merge_ranges(meetings):

    # Merge meeting ranges
    merged = []
    sort = sorted(meetings)
    curr_start = sort[0][0]
    curr_end = sort[0][1]

    for start, end in sort[1:]:
        if start <= curr_end:
            if end > curr_end:
                curr_end = end
        else:
            merged.append((curr_start, curr_end))
            curr_start = start
            curr_end = end
    
    merged.append((curr_start, curr_end))
    

    return merged