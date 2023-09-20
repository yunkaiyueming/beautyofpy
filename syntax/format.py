# coding=utf8

var1 = 'Hello World!'
var2 = 'Python Runoob'

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

name = 'Zara'
kg = 21
end = 'ok'
# 字符串格式化
print "My name is %s and weight is %d kg, Thx %s" % (name, kg, end)  # 更好
print  "My name is " + name + " and weight is " + str(kg) + " kg, Thx " + end

# unicode字符
print u'Hello World !我们的'
print 'Hello World !我们的'
