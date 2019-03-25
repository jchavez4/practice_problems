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

def reverse(list_of_chars):

    # Reverse the input list of chars in place
    i = 0
    j = len(list_of_chars) - 1
    print(i)
    print(j)
    
    while i < len(list_of_chars)/2 and j > 0:
        tmp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[j]
        list_of_chars[j] = tmp
        
        i+=1
        j-=1