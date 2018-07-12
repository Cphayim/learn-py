# 函数式编程

# 闭包 = 函数 + 环境变量(函数定义时外部变量)
# 保留现场


def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve
