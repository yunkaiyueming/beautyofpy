#coding=utf8

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

print '------------------tuple的操作------------------------------'
print tup1[2],tup1[1]
print tup1+tup2+tup3
print len(tup1)
print tup1[2:]

for x in tup1:
    print x


del tup1;
#print tup1