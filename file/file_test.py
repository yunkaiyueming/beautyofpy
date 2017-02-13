#coding=utf8
import os
import dir_test

dir_path = "E:/python_code/pysnippet/file"
new_file = dir_path+"/dir_test.py"
print '------------ file--------------------'

# fd = os.open(new_file, os.O_RDWR, 0777)
# print os.write(fd, "write something with py")
# print os.read(fd, 1024)

#fd = open(new_file, 'w+')
#fd.write("write something with py 你好")

#print os.remove(new_file)
print os.path.isfile(new_file)
print os.path.exists(new_file)
print os.path.split(new_file)
print os.path.getsize(new_file)
print os.stat(new_file)
print os.path.basename(new_file)
print os.path.dirname(new_file)
print os.path.join("home/ss/","12.txt")
print os.path.abspath(new_file)
print os.path.realpath(new_file)

print "fiel_test.py:"+__name__