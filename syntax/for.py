#coding=utf8

for letter in 'Python':  # 第一个实例
        print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
        print '当前水果 :', fruit

count = 0
while (count < 9):
        print 'The count is:', count
        count = count + 1

for num in range(10,20):  # 迭代 10 到 20之间的数字
        print num

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称

if True:
        print 'hello'

for letter in 'Python':  # 第一个实例
        if letter == 'h':
                break
        print '当前字母 :', letter

for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print '当前字母 :', letter

for i in range(1,10):
        for j in range(20,30):
                print i,j


print range(1,6) #返回数组
print xrange(1,6) #返回生成器