#coding=utf8

import Queue
import  threading
import time
import sys

map_reduce = Queue.Queue(10)
#map_reduce = Queue.Queue(10)

def produce_msg():
        i = 0
        while True:
                i = i+1
                map_reduce.put(i)
                print "produce:"+str(i)+" "

                if i>2000:
                        break

def consumer_msg():
        i = 0
        while True:
                i = i+1
                map_reduce.get(i)
                print "consumer:"+str(i)," queue_size:"+str(map_reduce.qsize())+" "

def start_map_reduce():
        threads = []
        p_thread = threading.Thread(target=produce_msg)
        threads.append(p_thread)
        c_thread = threading.Thread(target=consumer_msg)
        threads.append(c_thread)

        for t in threads:
                t.setDaemon(True)
                t.start()

        # t.join()  # 主线程的job都做完了，才结束
        # print "main thread over"


if __name__=="__main__":
        start_map_reduce()

        print "last_queue_size:" + str(map_reduce.qsize())
        #消费线程一直阻塞，下面的不会执行
        map_reduce.join()
        print "queue over"
