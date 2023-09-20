#coding=utf8

str_data =  "python"
str_data2 = ""

def demo_pass():
        pass

def change_data():
        str_data = "hello" #局部变量
        str_data2 = "11231"

def change_data2():
        global str_data
        str_data = "beauty"

def get_data():
        print str_data, str_data2 #使用全局变量

def default_func_var_demo(name, age=12, pwd="tt"):
        print name,age,pwd

#关键字函数
def key_words_demo(type , **keywords):
        print type, keywords

#可变参数/可变长参数/不定参数
def kebian_var_demo(type, *arguments):
        print type, arguments

def other_func_var_demo(type,  *arguments, **keywords):
        print type, arguments,keywords

get_data()
change_data()
get_data()
change_data2()
get_data()

default_func_var_demo("aa")
default_func_var_demo("aa", 234)
default_func_var_demo("aa", pwd="sd")
print dir()


key_words_demo(123,  name='aa', age='22')
kebian_var_demo(123, 'aa', 'tt')
other_func_var_demo(123, 'aa', 'tt', name='aa', age='22')

print '-----------builtins中包含的内置函数和变量名----------------------'
for f  in dir(__builtins__):
        print f

