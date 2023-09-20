#coding=utf8
import types


for i in types.__all__:
    print i, type(i)

print type([12,434])==types.ListType
print type([123,53])=='ListType'
print  isinstance([342,45],list)