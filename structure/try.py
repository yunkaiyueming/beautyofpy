#coding=utf8

try:
        open("fdsafds/fdsaf/s.xtx")
except:
        print "file open wrong"


try:
     print 'Normal execution block'
except "A":
        print 'execpt a'
except "B":
        print 'execpt b'
except:
        print 'execpt other'
else:
        print 'no except, run here'
finally:
     print("finally")