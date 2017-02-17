# coding=utf8

import zipfile
import glob
import os

def scan_dir(source_dir):
        return glob.glob(source_dir)


def zip_dir_demo():
        source_dir = 'E:\www2\GitHub\webchat'
        target_path = 'E:\python_code\pysnippet\zip\dir.zip'

        f = zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(source_dir):
                for filename in filenames:
                        f.write(os.path.join(dirpath, filename))
        f.close()


def unzip_demo():
        source_zip = "E:/python_code/pysnippet/zip/dir.zip"
        target_dir = "E:/python_code/pysnippet/zip/"

        my_zip = zipfile.ZipFile(source_zip)
        print my_zip.namelist()

        for name in my_zip.namelist():
                print os.path.dirname(name)
                if not os.path.exists(target_dir + "/" + os.path.dirname(name)):
                        os.mkdir(target_dir + "/" + os.path.dirname(name))

                f_handle = open(target_dir + name, "wb")
                f_handle.write(my_zip.read(name))
                f_handle.close()
        my_zip.close()


zip_dir_demo()
unzip_demo()
