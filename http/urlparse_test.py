#coding=utf8

import urlparse

url = "http://www.baidu.com/get_data/api?key=df&name=bb"
parsed_data = urlparse.urlparse(url)
print parsed_data

print urlparse.urlunparse(parsed_data)