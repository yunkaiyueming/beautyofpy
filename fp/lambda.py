#coding=utf8

import fp_param
import sys

lam_func = lambda x,y:x+y;
print lam_func(2,5)

def add(x, y):
        #doc:add函数
        return x+y

def lambda_add_func(x):
        return lambda y:x+y;

print add(2 ,5)
func = lambda_add_func(2)
print func(5)

print dir()
print __name__,__builtins__, __doc__, __file__, __package__
print "搜索路径",sys.path