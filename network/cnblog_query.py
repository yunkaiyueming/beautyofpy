#coding=utf8
from pyquery import PyQuery as pq

cnblog_url = "http://www.cnblogs.com/sitehome/p/"

#串行抓取cnblog前50页的博客url和标题
for i in range(1,11,1):
    print ("page: %d" %i)
    page_cnblog_url  = cnblog_url+("%d" %i)
    links = pq(page_cnblog_url)("a.titlelnk")
    for ret in links.items():
        print ret.attr('href'), ret.text()