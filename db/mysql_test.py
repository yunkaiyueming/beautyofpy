 #coding=UTF8
import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root', password='123456', database='test') #连接数据库
cursor=conn.cursor()
cursor.execute('select * from `order`') #表查询
values=cursor.fetchall()
print values
print values[0][1]
print values[0]

cursor.execute('insert into `order` (order_num, price, goog_info,create_time,user) values (%s, %s,%s,%s,%s)', ['201320156','27.25',"台灯","2017-02-21 12:22:10","张三"])
cursor.execute('select * from `order`') #表查询
print cursor.fetchall()