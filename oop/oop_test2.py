# coding=utf8

# 调用父类
class Base:
    def say(self):
        print("Base")


class Child(Base):
    def say(self):
        Base.say(self)
        #super(Child, self).say() #报错
        print("Child")


child = Child()
child.say()
