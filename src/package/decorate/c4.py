#!/usr/bin/env python3
from time import time
from functools import reduce


def time_decorator(is_compute=False):
    """时间戳装饰器
    为一个函数的调用添加计时功能，输出执行开始和结束时的 Unix 时间戳（毫秒）
    Arguments:
        isCompute {bool} -- 是否计算时间差值
    """

    def now_time():
        return round(time() * 1000)

    def dec_wrapper(func):
        def func_wrapper(*args, **kw):
            start_time = now_time()
            print('开始：' + str(start_time))
            res = func(*args, **kw)
            end_time = now_time()
            print('结束: ' + str(end_time))
            is_compute and print('执行耗时: ' + str(end_time - start_time) + 'ms')
            return res

        return func_wrapper

    return dec_wrapper


@time_decorator(True)
def test(l):
    return reduce(lambda x, y: x + y, l)


if __name__ == '__main__':
    print(test(range(0, 1000000)))
