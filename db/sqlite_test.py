#coding=UTF8

import sqlite3
import urllib2

resp=urllib2.urlopen("http://www.xxx.com/get_sql_data")
db_create_sql = resp.read()
print db_create_sql

conn = sqlite3.connect('test3.db')
curs= conn.cursor()
curs.executescript(db_create_sql) #执行多条sql
conn.close()