import re

# re.match
# re.search

s = '8C4996487D3973'

# match 从字符串的第一个字符开始搜索，一旦不符合规则立刻返回 None
r = re.match('\d', s)
print(r.span())

# serach 搜索整个字符串，直到找到第一个匹配的结果返回
r1 = re.search('\d', s)
print(r1.group())
