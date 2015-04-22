#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-22
#desc : thread pool
import os
import sys
import time
import threading
from Queue import Queue

g_lockPrint = threading.Lock()
def syc_log(msg):
    g_lockPrint.acquire()
    print(msg)
    g_lockPrint.release()
    
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args 
    def set(self, func, args):
        self.func = func
        self.args = args        
    def run(self):
        self.args = (self,) + self.args    # 加上MyThread自身
        #syc_log("self.args %s" % str(self.args))
        self.res = apply(self.func, self.args)
    def getResult(self):
        return self.res
    
class ThreadPoll(object):         
    def __init__(self, numThreads):
        self.numThreads_ = numThreads
        self.threadPoll_ = []
        self.jobList_ = Queue(-1)
        self.jobLock_ = threading.Lock()
        self.sem_ = threading.Semaphore()
        self.createThreads()
    def addJob(self, func, args):
        self.jobList_.put((func, args))
    def getJob(self):
        func, args = self.jobList_.get()
        return (func, args)
    def run(self):
        for i in xrange(len(self.threadPoll_)):
            self.threadPoll_[i].start()
    def stop(self):
        for i in xrange(len(self.threadPoll_)):
            self.threadPoll_[i].join()
    def createThreads(self):
        for i in xrange(self.numThreads_):
            self.threadPoll_.append(MyThread(ThreadPoll.threadFunc, (self,), name = 'thread_%d' % i))
    @staticmethod
    def threadFunc(thrd, thrdPoll):
        #syc_log("[%s] thread starting...." % threading.currentThread().getName())
        syc_log("[%s] thread starting...." % thrd.getName())
        while 1:
            func, args = thrdPoll.getJob()
            syc_log("[%s] (%s, %s)" % (threading.currentThread().getName(), func, args))
            #thread.set(func, args)
            res = apply(func, (args))
# End class ThreadPoll
def threadFunc(self, threadpoll):
    #syc_log("[%s] thread starting...." % threading.currentThread().getName())
    syc_log("[%s] thread starting...." % threading.currentThread().getName())
    while 1:
        func, args = threadpoll.getJob()
        syc_log("[%s] (%s, %s)" % (threading.currentThread().getName(), func, args))
        #thread.set(func, args)
        res = apply(func, (args))

def printHello():
    syc_log("[%s] thread printHello" % threading.currentThread().getName())
def printNum(num):
    syc_log("[%s] thread printNum [%d]" % (threading.currentThread().getName(), num))
def printSum(num1, num2):
    syc_log("[%s] thread printSum [%d]" % (threading.currentThread().getName(), num1+num2))
    
def test_threadpoll():
    poll = ThreadPoll(3)
    poll.run()
    time.sleep(2)  # wait for all threads starting

    poll.addJob(printHello, ())
    poll.addJob(printNum, (1,))
    time.sleep(1)
    poll.addJob(printNum, (2,))
    #return
    
    time.sleep(5)
    for i in xrange(100):
        if i % 2 == 0:
            poll.addJob(printNum, (i,))
        else:
            poll.addJob(printSum, (i,i+1))
            
if __name__ == '__main__':
    test_threadpoll()
    syc_log("######## GAME OVER ########")
