# coding=utf8

from gevent import monkey;

monkey.patch_socket()
import gevent
import time

def f(n):
        for i in range(n):
                print gevent.getcurrent(), i


def f2(n):
        for i in range(n):
                print gevent.getcurrent(),i
                gevent.sleep(0)

print '------------依次运行----------------'
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

print '-------------交替运行----------------'
g3 = gevent.spawn(f2, 5)
g4 = gevent.spawn(f2, 5)
g5 = gevent.spawn(f2, 5)
g3.join()
g4.join()
g5.join()