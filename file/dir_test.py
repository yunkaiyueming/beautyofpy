#coding=utf8
import os

dir_path = "E:/python_code/pysnippet"
new_dir = dir_path + "/file/test"
print '--------------dir-----------'

print os.listdir(dir_path);
#print os.mkdir(new_dir)
#print os.rmdir(new_dir)
print os.path.isdir(dir_path)
print os.getcwd()
#print os.name()
print os.path.split(dir_path)
print os.getenv('path')
print os.linesep
#print os.rename(new_dir, dir_path+"file/test2")

print "dir_test.py:"+__name__