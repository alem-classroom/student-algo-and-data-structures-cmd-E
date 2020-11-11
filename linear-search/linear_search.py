def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for index in range(len(lst)):
    if lst[index] == to_find:
      return index + 1
  return -1
print(linear_search([1, 3, 4, 5, 23, 12], 1))