list_x = list(range(1, 30))
list_y = list(range(1, 10))


def square(x):
    return x**2


# for x in list_x:
#     print(square(x))

# r = map(square, list_x)
# print(list(r))

# r = map(lambda x: x**2, list_x)
# print(list(r))

r = map(lambda x, y: x**2 + y, list_x, list_y)
print(list(r))
