import traceback
import time

def traceback_demo():
        try:
                1 / 0
        except Exception, e:
                print Exception, e

def traceback_demo2():
        try:
                1 / 0
        except Exception, e:
                traceback.print_exc()


traceback_demo()

time.sleep(1)
print '------------------'
traceback_demo2()