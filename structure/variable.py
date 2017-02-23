#coding=utf8

print '-----------------int ,float----------------------------'
data_int ,data_float= 1213, 5.62
print data_int, data_float

print '-----------------string----------------------------'

data_1 = data_2 = "11111"
print data_1,data_2
data_2="333333"
print data_1,data_2

print '-----------------list----------------------------'
data_list = data_list2 = [1,"aa","hehe", 1231, 43]
print data_list,data_list2
data_list2 = "fdafd"
print data_list,data_list2

data_list3 = data_list4 = []
data_list4.append("44")
print data_list3, data_list4

a,b,c,d,e = data_list
print a,b,c,d,e

print '-----------------map----------------------------'
data_map = {'name':'zhangshan', 'age':123}
print data_map

print '-----------------tuple----------------------------'
data_tuple = ("aa",2423,"naif")
print data_tuple