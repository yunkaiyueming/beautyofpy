# coding=utf8

from gevent import monkey;
monkey.patch_socket()
import gevent
import urllib2
from pyquery import PyQuery as pq
import time

cnblog_url = "http://www.cnblogs.com/sitehome/p/"

def pq_cnblog_claw(page):
        page_cnblog_url = cnblog_url + ("%d" % page)
        links = pq(page_cnblog_url)("a.titlelnk")
        print "page", ("%d" % page)
        for ret in links.items():
                print ret.attr('href'), ret.text()

def join_with_every(query_num):
        for i in range(query_num):
                g = gevent.spawn(pq_cnblog_claw, i)
                g.join()

#自动切换
def join_with_all():
        events = []
        for i in range(query_num):
                ev = gevent.spawn(pq_cnblog_claw, i )
                events.append(ev)
        gevent.joinall(events)

start_time = time.time()
query_num = 10

join_with_all()
#join_with_every(query_num)

end_time = time.time()
print "all_tiem:",end_time-start_time