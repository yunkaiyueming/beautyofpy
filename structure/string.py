#coding=UTF8
str = "niss,WTS,dfe"
str2 = str+"sfdso他的fwef"
print str
print str2

print '--------------------string操作------------------------------'
print str.lower()
print str.upper()
print str.islower()
print str.isupper()
print str.__class__
print str.__len__()
print str.split(",")
print str.find("WT")
print str.replace("s", "找")