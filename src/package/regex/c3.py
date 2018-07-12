import re

s = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('A[^c-f]c', s, re.I | re.S)
print(r)
