#coding=utf8

list_data = ['aa','bb','cc','dd']
map_data = {'nama':'xx', 'age':20, 'pwd':'tt'}

for t in list_data:
        print t

for t in range(len(list_data)):
        print t,list_data[t]

print '--------------map----------------------------'
for d in map_data:
        print d

for k,v in map_data.items():
        print k,v

print '----------------range--------------------------'
for i in range(20):
        print i