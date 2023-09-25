#!/usr/bin/python3
import sys
import re
import math
from urllib.request import urlopen
from datetime import date
import _thread
import os

# 基本变量类型
inti=1
stringj = "aa"
stringdata = "aa"+"bb"
floatj=20.9
print(floatj,type(floatj))

###字符串输出的几种方式
print("Hello, World Python3!")
print(r"this is a line with \n two")
print("this is a line with \n tow")
name="zhangsan"
print(f"wo my name is {name}")

string = '''
print(tmath.fabs(-10))
print(nrandom.choice(li))
'''
print(string)

if True:
    print ("True")
else:
    print ("False")

# 不换行输出
print( "1111", end=" " )
print( "2222")

### 输出命令行参数信息
def show_sys_func():
    print('================Python import mode==========================')
    print ('命令行参数为:')
    for i in sys.argv:
        print (i)
    print ('\n python 路径为',sys.path)

##list列表操作 列表可以修改，而字符串和元组不能
def test_list_func():
    list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
    tinylist = [123, 'runoob']

    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表

    for v in list:
        print(v)

    list.append(444)
    list.count(222)
    list.reverse()
    for v in list:
        print(v)

##元组操作 元组使用小括号，列表使用方括号 元组的元素不能修改
def test_tup_func():
    print("-------元组操作---------")
    tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
    tinytuple = (123, 'runoob')

    print (tuple)             # 输出完整元组
    print (tuple[0])          # 输出元组的第一个元素
    print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
    print (tuple[2:])         # 输出从第三个元素开始的所有元素
    print (tinytuple * 2)     # 输出两次元组
    print (tuple + tinytuple) # 连接元组
    print(len(tuple))

    for v in tuple:
        print(v)

##集合操作
def test_set():
    print("-------集合操作---------")
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
    print(sites)   # 输出集合，重复的元素被自动去掉
    sites.add("sds")
    sites.remove("Google")

    # 成员测试
    if 'Runoob' in sites :
        print('Runoob 在集合中')
    else :
        print('Runoob 不在集合中')

    sites.update(["11","22","33"])

    for v in sites:
        print(v,type(v))
    
    sites.clear()

##字典操作
def dict_test():
    print("-------字典操作---------")
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2]     = "2 - 菜鸟工具"

    tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

    print (dict['one'])       # 输出键为 'one' 的值
    print (dict[2])           # 输出键为 2 的值
    print (tinydict)          # 输出完整的字典
    print (tinydict.keys())   # 输出所有键
    print (tinydict.values()) # 输出所有值
    del dict[2]

    for x in tinydict:
        print(x)
        
    for v in tinydict.values():
        print(v)

    for v in tinydict.keys():
        print(v)
    
    #同时遍历取出k，v
    for k, v in tinydict.items():
        print(k, v)

##迭代器是一个可以记住遍历的位置的对象。
def iter_test():
    print("-------迭代器操作---------")
    li = [1, 2, 3]
    it = iter(li)
    for val in it:
        print(val)

    it2 = iter(li)
    while True:
        try:
            print (next(it2))
        except StopIteration:
            break

nihao="hao1"
##不可变类型：如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身
##可变类型：如列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
def func_param_test(name,age,listdata,tupledata,pwd="12312"):
    print("-------默认传参---------")
    global nihao
    nihao="hao2"

    listdata[3]=5
    tupledata = (5,6,7)
    return name,age,pwd


class Person:
    """人员信息"""
    # 姓名(共有属性)
    name = ''
    # 年龄(共有属性)
    age = 0

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    # 重载专有方法: __str__
    def __str__(self):
        return "这里重载了 __str__ 专有方法, " + str({'name': self.name, 'age': self.age})

    def set_age(self, age):
        self.age = age

class Account:
    """账户信息"""
    # 账户余额(私有属性)
    __balance = 0
    # 所有账户总额
    __total_balance = 0

    # 获取账户余额
    # self 必须是方法的第一个参数
    def balance(self):
        return self.__balance

    # 增加账户余额
    def balance_add(self, cost):
        # self 访问的是本实例
        self.__balance += cost
        # self.__class__ 可以访问类
        self.__class__.__total_balance += cost

    # 类方法(用 @classmethod 标识，第一个参数为 cls)
    @classmethod
    def total_balance(cls):
        return cls.__total_balance

    # 静态方法(用 @staticmethod 标识，不需要类参数或实例参数)
    @staticmethod
    def exchange(a, b):
        return b, a

class Teacher(Person, Account):
    """教师"""
    # 班级名称
    _class_name = ''

    def __init__(self, name):
        # 第一种重载父类__init__()构造方法
        # super(子类，self).__init__(参数1，参数2，....)
        super(Teacher, self).__init__(name)

    def get_info(self):
        # 以字典的形式返回个人信息
        return {
            'name': self.name,  # 此处访问的是父类Person的属性值
            'age': self.age,
            'class_name': self._class_name,
            'balance': self.balance(),  # 此处调用的是子类重载过的方法
        }

    # 方法重载
    def balance(self):
        # Account.__balance 为私有属性，子类无法访问，所以父类提供方法进行访问
        return Account.balance(self) * 1.1

class Student(Person, Account):
    """学生"""
    _teacher_name = ''

    def __init__(self, name, age=18):
        # 第二种重载父类__init__()构造方法
        # 父类名称.__init__(self,参数1，参数2，...)
        Person.__init__(self, name, age)
    
    def get_info(self):
        # 以字典的形式返回个人信息
        return {
            'name': self.name,  # 此处访问的是父类Person的属性值
            'age': self.age,
            'teacher_name': self._teacher_name,
            'balance': self.balance(),
        }

def oop_test():
    print("==========测试面向对象========")
    # 教师 John
    john = Teacher('John')
    john.balance_add(20)
    john.set_age(36)  # 子类的实例可以直接调用父类的方法
    print("John's info:", john.get_info())

    # 学生 Mary
    mary = Student('Mary', 18)
    mary.balance_add(18)
    print("Mary's info:", mary.get_info())

    # 学生 Fake
    fake = Student('Fake')
    fake.balance_add(30)
    print("Fake's info", fake.get_info())

    # 三种不同的方式调用静态方法
    print("john.exchange('a', 'b'):", john.exchange('a', 'b'))
    print('Teacher.exchange(1, 2)', Teacher.exchange(1, 2))
    print('Account.exchange(10, 20):', Account.exchange(10, 20))

    # 类方法、类属性
    print('Account.total_balance():', Account.total_balance())
    print('Teacher.total_balance():', Teacher.total_balance())
    print('Student.total_balance():', Student.total_balance())
    # 重载专有方法
    print(fake)

def py_stand_lib():
    print("==========测试标准库========")

    # 返回当前的工作目录
    print(os.getcwd())

    # 写文件
    with open("test.txt", "wt") as out_file:
        out_file.write("该文本会写入到文件中\n看到我了吧！")
 
    # Read a file
    with open("test.txt", "rt") as in_file:
        text = in_file.read()


    ##字符串正则匹配
    ret=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    print(ret)

    ##数学
    num = math.cos(math.pi / 4)
    print(num)

    ##网络请求
    for line in urlopen('http://baidu.com'):
        line = line.decode('utf-8')
        print(line)
        break

    ###日期
    now = date.today()
    print(now)

if __name__ == '__main__':
    print('程序自身在运行')

    dict_test()

    test_tup_func()

    test_set()

    iter_test()

    listdata=[1,2,3,4] ##值被改版
    tupledata=(1,2,3,4) ###值没改变
    a1 = func_param_test("aa",10,listdata,tupledata)
    print(a1,type(a1))
    print(nihao)
    print(listdata)
    print(tupledata)

    oop_test()
    
    py_stand_lib()
    
else:
    print('我来自另一模块')


#pip install 包名
#pip install 包名 == 包的版本号
#pip install —upgrade 包名 >= 包的版本号
#pip uninstall 包名
#pip list