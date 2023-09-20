import urllib2
import urllib

def http_request_get1(url):
    response = urllib2.urlopen(url)
    print response.read()
    #print response.getheaders()

def http_request_post1(url):
    post_data = urllib.urlencode({})
    response = urllib2.urlopen(url, post_data)
    print response.read()
    #print response.getheaders()

url = "http://www.baidu.com"
http_request_get1(url)
http_request_post1(url)