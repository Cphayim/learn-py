from enum import Enum, IntEnum, unique

# Enum 枚举类 枚举值可以是任何类型
# IntEnum 枚举类 枚举值只能是 int 型
# unique 装饰器 不能有相同值的枚举名


@unique
class VIP(IntEnum):
    # 枚举类成员属性建议使用大写
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 枚举类型
# print(type(VIP.GREEN))
# print(VIP.GREEN)
# 枚举名
# print(type(VIP.GREEN.name))
# print(VIP.GREEN.name)
# 枚举值
# print(VIP.GREEN.value)

# for v in VIP:
#     print(v.name)
#     print(v.value)

# 枚举转换
a = 1
print(VIP(a))  # VIP.YELLOW
