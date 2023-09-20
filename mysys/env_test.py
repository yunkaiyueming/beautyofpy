#coding=utf8

import sys
import os
import mycrypt.common
from mycrypt import machine #复制到当前模块，这样可以省略mycrypt

print mycrypt.common.my_base64_encode("fdf")
print machine.get_machine_cpu()

#判断模块是否是内建，并获取模块路径
def dump(module):
    print module, "=>",
    if module in sys.builtin_module_names:  #查找内建模块是否存在
        print "<BUILTIN>"
    else:
        module = __import__(module)         #非内建模块输出模块路径
        print module.__file__

def test2():
        #print  sys.argv[0], sys.argv[1]
        print sys.builtin_module_names
        print sys._current_frames()
        print sys.platform
        print sys.path
        print sys.modules.keys(),sys.modules.values()

        dump("sys")
        dump("pyquery")