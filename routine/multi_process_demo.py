#coding=utf8

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    str = 'Run child process %s (%s)...' % (name, os.getpid())
    print(str)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Process will start.')
    p.start()

    p2 = Process(target=run_proc, args=('test2',))
    print('Process2 will start.')
    p2.start()

    p.join()
    p2.join()
    print('Process end.')
