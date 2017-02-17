#coding=utf8

import zipfile

file = '../README.md'

f = zipfile.ZipFile('readme.zip', 'w', zipfile.ZIP_DEFLATED)
f.write(file, 'readme.md')
f.close()