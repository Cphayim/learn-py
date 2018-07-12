# 生成器
# print 0~10000

# n = [i for i in range(0, 10001)]

# print(n)


def gen(max):
    n = 0
    while n <= max:
        n += 1
        yield n


g = gen(10000)

# 每调用一次 next 会返回一个数字
# print(next(g))
# print(next(g))

for i in g:
    print(i)
