#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Cphayim at 2018/06/18
"""

# def fact(n):
#     if n <= 1:
#         return n
#     return n * fact(n - 1)

# print(fact(5))

# for x in ran5

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(0, len(a), 2):
    print(a[x], end=' | ')

b = a[0:len(a):2]

print(b)
