import httplib,urllib

def http_get_request():
        conn = httplib.HTTPConnection("www.douban.com")
        conn.request("GET", "/index.html")
        r1 = conn.getresponse()
        print r1.status, r1.reason
        data1 = r1.read()
        conn.request("GET", "/parrot.spam")
        r2 = conn.getresponse()
        data2 = r2.read()
        conn.close()

def http_post_request():
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("www.baidu.com")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()

http_post_request()
http_get_request()