# -*- coding:utf-8 -*-

from os import environ
from selenium import webdriver

browser = webdriver.PhantomJS(r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
browser.get('http://www.baidu.com')
