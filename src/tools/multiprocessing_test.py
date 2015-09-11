#!/usr/bin/env python
#coding=utf-8
import multiprocessing
import time
# 多进程编程(windows下不好用)， see http://www.cnblogs.com/kaituorensheng/p/4445418.html
# http://www.cnblogs.com/kaituorensheng/p/4465768.html
def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
    p.join()
