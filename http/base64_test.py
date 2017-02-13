#coding=utf8

import base64

str = "it我来自ni fdsa"
encode_str = base64.b64encode(str)
print encode_str
print base64.b64decode(encode_str)