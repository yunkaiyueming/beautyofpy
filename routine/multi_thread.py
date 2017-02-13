#coding=utf8

import threading
import time
import sys

def pay_movie():
    for i in range(10):
        print "movie...."
        time.sleep(1)

def pay_music():
    for i in range(10):
        print "music......"
        time.sleep(1)

def simple_run():
    pay_movie()
    pay_music()
    print "main over"

def parallel_run():
    threads = []
    t1 = threading.Thread(target=pay_movie)
    threads.append(t1)
    t2 = threading.Thread(target=pay_music)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

start_time = time.time()
if sys.argv[1]=="1":
    print "simple"
    simple_run() # time: 20.0010001659
else:
    print "parallel run"
    parallel_run() # time: 10.0009999275
end_time = time.time()
print end_time-start_time