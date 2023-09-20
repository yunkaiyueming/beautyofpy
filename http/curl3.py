import requests

import urllib2
import json

def get():
    print requests.get("http://www.baidu.com").text

def post_with_auth():
    url = 'http://localhost:8080'
    r = requests.post(url, data={}, auth=HTTPBasicAuth('admin', 'admin'))
    print r.status_code
    print r.headers
    print r.reason

def douban_api_culr():
    html = urllib2.urlopen(r'https://api.douban.com/v2/book/isbn/9787218087351')
    ret = html.read(); print ret
    hjson = json.loads(ret)

    print hjson['rating']
    print hjson['images']['large']
    print hjson['summary']

get()
douban_api_culr()