def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    middleIndex = int(len(lst) / 2)
    suspect = lst[middleIndex]
    if to_find not in lst:
        return -1
    if suspect == to_find:
        return lst[middleIndex]
    elif suspect > to_find:
        return binary_search(lst[:middleIndex], to_find)
    elif suspect < to_find:
        return binary_search(lst[middleIndex:], to_find)
