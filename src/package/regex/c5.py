import re

s = 'A8C4996487D3973'


def convert(value):
    metched = value.group()
    if int(metched) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s)

print(r)
