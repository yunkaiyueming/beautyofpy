# coding=utf-8

import os
import linecache

def get_content(path):
    '''读取缓存中文件内容，以字符串形式返回'''
    if os.path.exists(path):
        content = ''
        cache_data = linecache.getlines(path)
        for line in range(len(cache_data)):
            content += cache_data[line]
        return content
    else:
        print('the path [{}] is not exist!'.format(path))

def main():
    path = 'E:/python_code/pysnippet/http/urlparse_test.py'
    content = get_content(path)
    print(content)

if __name__ == '__main__':
    main()