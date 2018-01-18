# -*- coding:utf-8 -*-

from os import environ
from selenium import webdriver

# chromedriver = "D:\soft_bk\chromedriver.exe"
# environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
environ["chromedriver"] = chromedriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')