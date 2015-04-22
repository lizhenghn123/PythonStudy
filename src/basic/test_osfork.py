#! /usr/bin/env python
# coding=utf-8
# author=lizheng
# date=2015-04-21
# refer : <<Python网络编程基础(莫迟 译)>> Chapter20.forking
import os
import time
import signal
import socket

# python 中的fork语义和linux系统里的fork是一样的

# case 1 : 提示，由于调用了fork，因此此函数会返回两次
def test_fork():
    print "Before the fork, My PID is", os.getpid()
    if os.fork():
        print "Hello from the parent.  My PID is", os.getpid()
    else:
        print "Hello from the child.  My PID is", os.getpid()
    time.sleep(2)
    print "Hello from both of us."

#  case 2 : 
# 类似linux，如果父进程不回收已经退出的子进程，那么子进程就会成为僵尸进程。
# 提示，此时 ps -aux | grep childPid. 应会有所发现
def test_fork_zombie():
    print "Before the fork, My PID is", os.getpid()
    if os.fork():
        print "Hello from the parent.  My PID is", os.getpid()
        print "Sleeping 120 seconds..."
        time.sleep(120)
    else:
        print "Hello from the child.  My PID is", os.getpid()
        print "I am just exit now!"
    print "Hello from both of us."

#  case 3 : 
# 父进程使用singal方式等待子进程的退出
def chldhandler(signum, stackframe):
    """Signal handler.  Runs on the parent and is called whenever
    a child terminates."""
    while 1:
        # Repeat as long as there are children to collect.
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print "Reaped child process %d" % result[0]
    # Re-set the signal handler so future signals trigger this function
    signal.signal(signal.SIGCHLD, chldhandler)

def test_wait_child():
    # Install signal handler so that chldhandler() gets called whenever child process terminates.
    signal.signal(signal.SIGCHLD, chldhandler) #  每次子进程退出时产生SIGCHLD，触发事件
    print "Before the fork, My PID is", os.getpid()
    pid = os.fork()
    if pid:
        print "Hello from the parent.  The child will be PID %d" % pid
        print "Sleeping 10 seconds..."
        time.sleep(10)
        print "Parent Sleep done."
    else:
        print "Child sleeping 5 seconds..."
        time.sleep(5)
        print "Child Sleep done."

#  case 4 :
def reap():
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
            if not result[0]: break
        except:
            break
        print "Reaped child process %d" % result[0]

def test_fork_poll():
    host = ''                               # Bind to all interfaces
    port = 51423

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print "Parent at %d listening for connections" % os.getpid()

    while 1:
        try:
            clientsock, clientaddr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        # Clean up old children.
        reap()
        # Fork a process for this connection.
        pid = os.fork()
        if pid:
            # This is the parent process.  Close the child's socket
            # and return to the top of the loop.
            clientsock.close()
            continue
        else:
            # From here on, this is the child.
            s.close()                           # Close the parent's socket               
            # Process the connection
            try:
                print "Child from %s being handled by PID %d" % (clientsock.getpeername(), os.getpid())
                while 1:
                    data = clientsock.recv(4096)
                    if not len(data):
                        break
                    clientsock.sendall(data)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                traceback.print_exc()
            # Close the connection
            try:
                clientsock.close()
            except KeyboardInterrupt:
                raise
            except:
                traceback.print_exc()
            # Done handling the connection.  Child process *must* terminate
            # and not go back to the top of the loop.
            sys.exit(0)

if __name__ == '__main__':
    test_fork()
    test_fork_zombie()
    test_wait_child()
    test_fork_poll()