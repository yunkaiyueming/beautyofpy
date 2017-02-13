#coding=utf8

import Cookie
import urllib2
import cookielib

#获取Cookiejar对象（存在本机的cookie消息）
cj = cookielib.CookieJar()
print cj
#自定义opener,并将opener跟CookieJar对象绑定
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#安装opener,此后调用urlopen()时都会使用安装过的opener对象
urllib2.install_opener(opener)

url = "http://www.baidu.com"
urllib2.urlopen(url)
#获取cookie信息
print cj