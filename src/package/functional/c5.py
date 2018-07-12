from functools import reduce

list_x = list(range(1, 5))
list_y = list(range(1, 10))

r = reduce(lambda x, y: x * y, list_x, 2)
print(r)
