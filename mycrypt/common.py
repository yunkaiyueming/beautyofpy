import base64
import hashlib

def my_base64_encode(str):
    return base64.encodestring(str)

def my_base64_decode(str):
    return base64.decodestring(str)

def md5(str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

def sha1(str):
        m = hashlib.sha1()
        m.update(str)
        return m.hexdigest()

origin_str = "python is good"
print my_base64_encode(origin_str)
print my_base64_decode(my_base64_encode(origin_str))
print md5(origin_str)
print  sha1(origin_str)

x = hashlib.md5()
x.update('hello, ')
x.update('python')
print x.hexdigest()

print hashlib.md5('hello, python').hexdigest()
print hashlib.md5('hello, python').digest()