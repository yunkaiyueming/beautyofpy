#coding=UTF8
import datetime

now = datetime.date.today()
print now
print now.strftime('%Y-%m-%d')
print now.strftime('%b %A %B')
print now.strftime("%Y-%m-%d or %d%b %Y is a %A on the %d day of %B")

print datetime.date(2003, 12, 2)

start_date = datetime.date(2017, 1, 2)
sub_date = now-start_date
print sub_date.days #间隔的天数
print datetime.date.today().isocalendar() #返回tuple