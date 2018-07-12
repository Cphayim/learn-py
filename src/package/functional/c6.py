# list_x = list(range(1, 100))

# r = filter(lambda x: True if x % 2 == 0 else False, list_x)
# print(list(r))

import re

list_y = ['a', 'B', 'c', 'D']

r = filter(lambda y: True if re.match('^[a-z]$', y) else False, list_y)
print(list(r))
