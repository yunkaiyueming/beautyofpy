# coding=utf8

# 安装模块后
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
        "http://www.baidu.com",
        version=5,
        level='H',
        picture='gb.jpg',
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=None,
        save_dir=os.getcwd()
)
