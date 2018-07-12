import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        return func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function')


@decorator
def f2(name, age):
    print(name + ':' + str(age))


@decorator
def f3(name, age, **kw):
    print(name + ':' + str(age))
    print(kw)
    return 3


# f = decorator(f1)
# f()

# f1('test')
# f2('Hoyoe', 18)
print(f3('Hoyoe', 18, a=1, b=2, c='123'))
