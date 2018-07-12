from Human import Human
import json

class Student(Human):
    def __init__(self, school, name, age):
        self.__school = school
        # Human.__init__(self, name, age)
        super(self.__class__, self).__init__(name, age)

    def do_homework(self):
        super(self.__class__, self).do_homework()
        print('english homework')


student1 = Student('人民路小学', '石敢当', 18)
print(student1)
print(json.dumps(student1.__dict__, ))