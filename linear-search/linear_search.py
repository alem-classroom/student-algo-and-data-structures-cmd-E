def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for index in range(len(lst)):
    if lst[index] == to_find:
      # return index Функция должна возвращать индекс
      return lst[index]

  return -1
