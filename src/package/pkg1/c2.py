# import c1
# import t.tc1

# print(c1.a)
# print(t.tc1.b)

from c1 import a, b, c
# from c1 import * 不推荐
from t import tc1

print(a)
print(b)
print(c)
print(tc1.b)
