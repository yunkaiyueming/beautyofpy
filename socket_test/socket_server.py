#coding=utf8

import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8180))
sk.listen(10) #处理连接请求的个数

while 1:
        # wait to accept a connection - blocking call
        conn, addr = sk.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

        data = conn.recv(1024)
        print "Receive: "+ data
        if not data:
                break

        conn.sendall('Send: ' + data)

conn.close()
sk.close()