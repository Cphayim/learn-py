
# 字典映射来代替 switch

day = 6

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

day_name = switcher.get(day, 'Unkonwn')

print(day_name)
