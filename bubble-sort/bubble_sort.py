def bubble_sort(lst):
    # sort the list via bubble sort
    while not isSorted(lst):
        for i in range(len(lst)):
            if i != len(lst)-1:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

def isSorted(lst):
    for i in range(len(lst)):
        if i != len(lst)-1:
            if lst[i] > lst[i + 1]:
                return False
    return True
