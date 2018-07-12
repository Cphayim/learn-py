# 类、对象
# 实例化
# 类最基本的作用：封装


class Student():
    # 这里是类变量（静态成员）
    sum = 0

    # 构造函数
    def __init__(self, name, age):
        # 这里是实例变量（实例成员）
        self.name = name
        self.age = age
        self.__score = 0
        # self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum))

    # 实例方法的第一个形参必须是 self
    def do_homework(self):
        print('homework')

    def __do_english_homework(self):
        print('english homework')

    def marking(self, score):
        if score < 0:
            score = 0
        elif score > 100:
            score = 100

        print(self.__score)
        self.__score = score
        print(self.name + '本次考试分数为' + str(self.__score))
        print(self.__dict__)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级学生总数为：' + str(cls.sum))

    @staticmethod
    def add(x, y):
        print('This is a static method')


student1 = Student('石敢当', 18)
# student1.marking(30)
# print(student1.__dict__)
# student1.__score = -1
# print(student1.__dict__)
# student1.marking(101)
# student1.add(1, 2)
# Student.add(1, 2)
# Student.plus_sum()
# student2 = Student('喜小乐', 16)
# Student.plus_sum()
# student3 = Student('葛大猫', 26)
# Student.plus_sum()
# __dict__ 输出当前对象（或类）的所有实例变量（或类变量）
# print(student1.__dict__)
# python 会首先在实例变量中寻找，若找不到则会到类变量中寻找
