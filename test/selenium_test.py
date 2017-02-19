# -*- coding:utf-8 -*-

from os import environ
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')