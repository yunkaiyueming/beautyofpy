#coding=utf8

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(("127.0.0.1",8180))

sk.sendall("hello world")
while 1:
        data = sk.recv(1024)
        print "Receive: "+data

        if not data:
                break
        sk.sendall("Send: "+data)