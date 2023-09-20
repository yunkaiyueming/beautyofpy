#coding=utf8

import uuid

namespace = "zhangsan"
name = "tt"

print uuid.uuid4()
print uuid.uuid1()
#print uuid.uuid3(namespace, name)
#print uuid.uuid5(namespace, name)