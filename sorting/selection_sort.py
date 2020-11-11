def selection_sort(lst):
    # sort the list via selection sort
    if len(lst) == 1:
        return lst
    
    for i in range(len(lst)):
        theSmallest = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[theSmallest]:
                theSmallest = j
        lst[i], lst[theSmallest] = lst[theSmallest], lst[i]
    return lst
