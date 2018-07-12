import re

s = 'life is short, i use python'

r = re.search('(life(.*)python)', s)

if r:
    # print(r.group(0, 1, 2))
    print(r.groups())
