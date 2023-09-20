#coding=utf8

class people:
        name = "aa"
        age = 20 #公有
        __sex = "man" #私有

        #对象方法
        def get_name(self):
                return self.name

        def get_age(self):
                return self.age

        def get_sex(self):
                return self.__sex

        #类方法
        @classmethod
        def set_name(cls, name):
                cls.name = name

        #静态方法
        @staticmethod
        def get_class_name():
                return people.name

print '------------对象调用--------------------'
p_obj = people()

print p_obj.name
print p_obj.age
#print p_obj.__sex

print p_obj.get_name()
print p_obj.get_age()
print p_obj.get_sex()
print p_obj.get_class_name()
print p_obj.set_name("zhangsan")

print '--------------类调用--------------------------------'

print people.name
print people.age
#print people.__sex

#people.get_name()
#people.get_sex()
#people.get_age()
people.set_name("李四")
people.get_class_name()

print  people.name
print p_obj.name