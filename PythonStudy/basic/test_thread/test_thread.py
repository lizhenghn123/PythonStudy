#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-13
from time import sleep, ctime
import thread     # thread 模块已不建议使用
import threading  # 更高一级抽象和封装，提供了Thread类，Lock，Condition，Event，Timer等

#  case 1 ：test thread 
def loop0():
    print("start loop 0 at:%s\n" % ctime())
    sleep(4)
    print("loop 0 done at:%s" % ctime())
def loop1():
    print("start loop 1 at:%s\n" % ctime())
    sleep(2)
    print("loop 1 done at:%s" % ctime())
def test_thread1():
    print("start main at:%s" % ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at:%s" % ctime())

#  case 2 ：test thread 
# 使用锁同步主线程和辅线程的执行顺序
loops = [4, 2]
def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()
def test_thread2():
    print 'starting threads...'
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all DONE at:', ctime()

if __name__ == "__main__":
    print("----------case 1 ：test thread----------")
    test_thread1()
    print("----------case 2 ：test thread----------")
    test_thread2()