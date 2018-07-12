import time

# 开闭原则：对修改是封闭的，对扩展是开放的


def f1():
    print('This is a function')


def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
