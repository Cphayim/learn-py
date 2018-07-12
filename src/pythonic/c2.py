# 列表推导式

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# b = list(map(lambda i: i * i, a))

# b = [i ** 2 for i in a]

b = [i ** 2 for i in a if i >= 5]

print(b)
