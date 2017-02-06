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

origin_str = "pythonisgood"
print my_base64_encode(origin_str)
print my_base64_decode(my_base64_encode(origin_str))
print md5(origin_str)