#coding=utf8

#set无序，不重复

set_data1 = set("hello")
set_data2 = set(["aa", "bb", "cc",123, 456])
set_data3 =set(["bb", "dd", 456, 789, "ee"])
print set_data1,set_data2,set_data3


print set_data3 & set_data2 #交集
print set_data3 | set_data2 #并集
print  set_data3 ^ set_data2 #对称差集（项在1或2中，但不会同时出现在二者中）
print set_data3 - set_data2 #差集

print set_data3.intersection(set_data2)
print set_data3.union(set_data2)
print set_data3.difference(set_data2)
print set_data3.symmetric_difference(set_data2)

set_data1.add("world")
print set_data1

set_data1.update(["py", "beauty"])
print set_data1

set_data1.remove("l")
print set_data1

print len(set_data1)
for i in set_data2:
    print i

if "py" in set_data1:
    print 'true'
else:
    print 'false'

print set_data1.copy()
print hash(set_data2)