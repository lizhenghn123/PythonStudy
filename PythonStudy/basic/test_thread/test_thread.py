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
def test1_thread():
    print("start main at:%s" % ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at:%s" % ctime())

#  case 2 ：test thread : 使用锁同步主线程和辅线程的执行顺序
loops = [4, 2]
def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()
def test2_thread():
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

# case 3 : test threading : join， 给Thread传递函数对象
def loop3(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def test3_threading():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop3, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:            # start threads
        threads[i].start()
    for i in nloops:            # wait for all
        threads[i].join()       # threads to finish
    print 'all DONE at:', ctime()

# case 4 : test threading : 给Thread传递类对象
def loop4(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        apply(self.func, self.args)
def test4_threading():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:	# create all threads
        t = threading.Thread(
	    target=ThreadFunc(loop4, (i, loops[i]), loop.__name__))
        threads.append(t)
    for i in nloops:	# start all threads
        threads[i].start()
    for i in nloops:	# wait for completion
        threads[i].join()
    print 'all DONE at:', ctime()

# case 5 : test threading : 实现新类并继承自Thread
def loop5(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.res = apply(self.func, self.args)
    def getResult(self):
        return self.res
def test5_threading():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop5, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'all DONE at:', ctime()

# case 6 : test threading : 实现新类并继承自Thread，综合应用
def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))
def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))
def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = (fib, fac, sum)
n = 12
def test6_threading():
    nfuncs = range(len(funcs))
    print '*** SINGLE THREAD'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:', ctime()

    print '\n*** MULTIPLE THREADS'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,),
	    funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()

    print 'all DONE'
if __name__ == "__main__":
    print("----------case 1 ：test thread----------")
    #test1_thread()
    print("----------case 2 ：test thread----------")
    #test2_thread()
    print("----------case 3 ：test threading----------")
    #test3_threading()
    print("----------case 4 ：test threading----------")
    #test4_threading()
    print("----------case 5 ：test threading----------")
    #test5_threading()
    print("----------case 5 ：test threading----------")
    test6_threading()