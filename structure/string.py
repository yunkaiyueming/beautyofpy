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
print str.capitalize()
print str.find("o")
print str.count("s")
print str.isdigit();#是否只有数字组成的字符串