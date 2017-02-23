#coding=utf8

from selenium import webdriver

browser = webdriver.Firefox()
# browser = webdriver.Safari()
# browser = webdriver.Chrome()
# browser = webdriver.Ie()
# browser = webdriver.PhantomJs()

browser.get('http://baidu.com')

print browser.title
# do anything you want