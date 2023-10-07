 
# 功能 : 将当前工作目录下所有webp格式转为png or jpg
# -*- coding: UTF-8 -*-
import os
from PIL import Image

def convert_imge2():
    img = Image.open("历年房贷利率.webp")
    img.load()
    # 将赋值的图片修改后缀保存在原路径
    img.save('历年房贷利率.png')
    # 删除原webp图
    # os.remove(webpP历年房贷利率ath+"历年房贷利率.webp")

# 执行
convert_imge2()