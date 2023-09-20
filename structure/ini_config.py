import ConfigParser

db_host =''
db_port = ''
db_user = ''
db_pwd = ''

cf = ConfigParser.ConfigParser()
cf.read("mysql.ini")

db_host = cf.get("mysqlconf", "host")
db_port = cf.getint("mysqlconf", "port")
db_user = cf.get("mysqlconf", "user")
db_pwd = cf.get("mysqlconf", "pwd")

print db_host, db_port, db_user, db_pwd

s = cf.sections()
print 'section:', s

o = cf.options("login")
print 'options:', o

v = cf.items("mysqlconf")
print 'db:', v

