def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    # Reccursion variant
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
    else:
        return -1
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))