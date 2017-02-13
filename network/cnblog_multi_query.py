# coding=utf8

import threading
import sys
import time
from pyquery import PyQuery as pq

cnblog_url = "http://www.cnblogs.com/sitehome/p/"


def pq_cnblog_claw(page):
        page_cnblog_url = cnblog_url + ("%d" % page)
        links = pq(page_cnblog_url)("a.titlelnk")
        print "page", ("%d" % page)
        for ret in links.items():
                print ret.attr('href'), ret.text()


# 串行
def simple_query(num):
        for i in range(num):
                pq_cnblog_claw(i)

# 多线程
def multi_query(num):
        thread_query = []
        for i in range(num):
                t_num = threading.Thread(target=pq_cnblog_claw, args=(i,))
                thread_query.append(t_num)

        for t in thread_query:
                t.setDaemon(True)
                t.start()
        t.join()


query_num = 10
start_time = time.time()

if sys.argv[1] == "1":
        simple_query(query_num) #
else:
        multi_query(query_num) # 0.4539999  ？run_time之前后还在执行？

end_time = time.time()
print "\n run_time:", end_time - start_time
