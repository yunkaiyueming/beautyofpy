#coding=UTF8
import time

print time.time()
now_date_time = time.localtime(time.time());print now_date_time
print time.strftime('%Y-%m-%d %H:%M:%S', now_date_time)
print time.strftime('%A %B %Z', now_date_time)

customer_time = "2016-01-02 22:23:31"
timeArray = time.strptime(customer_time, "%Y-%m-%d %H:%M:%S")
print time.mktime(timeArray),type(timeArray)

timeArray = time.strptime(customer_time, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print otherStyleTime

timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print otherStyleTime == "2013-10-10 23:40:00"