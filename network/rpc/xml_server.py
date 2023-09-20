#coding=utf8
from SimpleXMLRPCServer import SimpleXMLRPCServer

def add(x, y):
    return x + y

if __name__ == '__main__':
    s = SimpleXMLRPCServer(('127.0.0.1', 8080))
    s.register_function(add)
    s.serve_forever()

#s是一个绑定了本地8080端口的服务器对象，
# register_function()方法将函数add注册到s中。
# serve_forever()启动服务器