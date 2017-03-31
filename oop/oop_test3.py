# coding=utf8

class Person:
        def __init__(self):
                self.name = "Tom"

        def getName(self):
                return self.name


class Student(Person):
        def __init__(self):
                Person.__init__(self)
                self.age = 12

        def getAge(self):
                return self.age


class Student2(Person):
        def __init__(self):
                super(Student2, self).__init__()
                self.age = 12

        def getAge(self):
                return self.age


if __name__ == "__main__":
        stu = Student() #调用未绑定的父类构造方法
        stu2 = Student2() #使用super函数调父类
        print stu.getName(), stu2.getName()
