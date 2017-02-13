#coding=utf8
import urllib

url = "http://www.baidu.com?key=淘宝&name=ba"
encode_str = urllib.quote(url)
print encode_str
print urllib.unquote(encode_str)

query_data = {"name":"我们", "age":20, 'pwd':"dsfsa"}
query_encode = urllib.urlencode(query_data)
print query_encode
print urllib.unquote(query_encode)