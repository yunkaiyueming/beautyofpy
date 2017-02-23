# coding=utf8

import uuid
import socket
import os
import getpass
import datetime
import multiprocessing

# 获取本机mac
def get_mac_address():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


# 获取本机ip
def get_machine_ip():
        myname = socket.getfqdn(socket.gethostname())
        myaddr = socket.gethostbyname(myname)
        return myaddr

# 获取当前用户
def get_machine_user():
        UserNmae1 = os.environ['USERNAME']
        return UserNmae1


# 获取当前时间
def get_machine_datetime():
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

#获取cpu个数
def get_machine_cpu():
        return multiprocessing.cpu_count()

print "Mac:", get_mac_address()
print "User:", get_machine_user()
print "IP:", get_machine_ip()
print "Datatime: ", get_machine_datetime()
print "Cpu Num:", get_machine_cpu()